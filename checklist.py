'''
    Program: Checklist
    Author : akr
    GitHub : https://github.com/a-k-r-a-k-r
    Blog   : https://a-k-r-a-k-r.blogspot.com
'''


#Simple Checklist
import tkinter
from tkinter import END, ANCHOR, filedialog
count=0


#Define fonts and colors
my_font = ('Times New Roman', 12)
root_color = 'black'
list_entry_bg = "lightblue"
list_entry_fg = "blue"
listbox_bg = "black"
listbox_fg = "red"
button_color = 'lightblue'



#Define window
root = tkinter.Tk()
root.title('My Checklist')
root.iconbitmap('resources/icons/checklist.ico')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg=root_color)


#Define functions
def add_item():
    global count
    count=count+1
    my_listbox.insert(END,str(count) + ") " + list_entry.get())
    list_entry.delete(0, END)


def remove_item():
    my_listbox.delete(ANCHOR)


def clear_list():
    global count
    my_listbox.delete(0, END)
    count=0


def save_list():
    global path
    path=filedialog.asksaveasfilename(initialdir="./saved_lists",title="Save List",filetype=(("Text File","*.txt"),("All Files","*.*")))
    path=path+".txt"
    with open("last_file_path.txt","w") as last_file:
        last_file.write(path)
    with open(path, 'w') as f:
        list_tuple = my_listbox.get(0, END)
        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + "\n")


def open_last_list():
    try:
        with open('last_file_path.txt', 'r') as f:
            path=f.read()
        with open(path,"r") as f:
            for line in f:
                my_listbox.insert(END, line)
    except:
        return

def open_saved():
    clear_list()
    path=filedialog.askopenfile(initialdir="./saved_lists",title="Checklists",filetype=(("Text File","*.txt"),("All Files","*.*")))
    path=path.name
    with open("last_file_path.txt","w") as last_file:
        last_file.write(path)
    with open(path,"r") as f:
        for line in f:
            my_listbox.insert(END, line)


#Define layout
#Create frames
input_frame = tkinter.Frame(root, bg=root_color)
output_frame = tkinter.Frame(root, bg=root_color)
button_frame = tkinter.Frame(root, bg=root_color)
input_frame.pack()
output_frame.pack()
button_frame.pack()

#Input frame layout
list_entry = tkinter.Entry(input_frame, width=35, borderwidth=3, font=my_font,bg=list_entry_bg,fg=list_entry_fg)
list_add_button = tkinter.Button(input_frame, text="Add Item", borderwidth=2,font=my_font, bg=button_color, command=add_item)
list_entry.grid(row=0, column=0, padx=5, pady=5)
list_add_button.grid(row=0, column=1, padx=5, pady=5, ipadx=5)

#Output frame layout
my_scrollbar = tkinter.Scrollbar(output_frame)
my_listbox = tkinter.Listbox(output_frame, height=15, width=45, borderwidth=3,font=my_font,bg=listbox_bg,fg=listbox_fg ,yscrollcommand=my_scrollbar.set)
#Link scrollbar to listbox
my_scrollbar.config(command=my_listbox.yview)
my_listbox.grid(row=0, column=0)
my_scrollbar.grid(row=0, column=1, sticky="NS")

#Button Frame layout
list_remove_button = tkinter.Button(button_frame, text="Remove Item", borderwidth=2,font=my_font, bg=button_color, command=remove_item)
list_clear_button = tkinter.Button(button_frame, text='Clear List', borderwidth=2,font=my_font, bg=button_color, command=clear_list)
save_button = tkinter.Button(button_frame, text='Save List', borderwidth=2,font=my_font, bg=button_color, command=save_list)
quit_button = tkinter.Button(button_frame, text='Open', borderwidth=2, font=my_font,bg=button_color, command=open_saved)
list_remove_button.grid(row=0, column=0, padx=2, pady=10)
list_clear_button.grid(row=0, column=1, padx=2, pady=10, ipadx=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=10)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=25)


#Open the previous list if available
open_last_list()

#Run the root window's main loop
root.mainloop()