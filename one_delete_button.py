###################
# Account Manager #
###################

import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox
from functools import partial
### Constants ###
HEIGHT = 700
WIDTH = 800
ENTRY_WIDTH = 25
LABEL_WIDTH = 25
root = tk.Tk()
root.title("Account Manager")
root.geometry("+400+200")
button_id = []
users = []


#################

def get_count():
    f = open("userinfo.txt", "r")
    count = 0
    for line in f:
        count += 1
    return count

# adds userinfo to appropriate label with delete button
# *From File*
def add_info(name, user, password, count):
    number_diplay = tk.Label(root, text = count)
    name_display = tk.Label(root, text = name)
    user_display = tk.Label(root, text = user)
    pass_display = tk.Label(root, text = password)
    # delete_button = tk.Button(root, text = "X",fg = "red", command = delete_entry)

    number_diplay.grid(row = (4 + count), column = 0)
    name_display.grid(row = (4 + count), column = 1)
    user_display.grid(row = (4 + count), column = 2)
    pass_display.grid(row = (4 + count), column = 3)

# adds userinfo to appropriate label with delete button
# *From Entry*
def add_new(name, user, password):
    count = get_count()
    
    number_display = tk.Label(root, text = count)
    name_display = tk.Label(root, text = name)
    user_display = tk.Label(root, text = user)
    pass_display = tk.Label(root, text = password)
    
    number_display.grid(row =(4 + count), column = 0)
    name_display.grid(row = (4 + count), column = 1)
    user_display.grid(row = (4 + count), column = 2)
    pass_display.grid(row = (4 + count), column = 3)


# replaces the line in the file with an empty string(deletes it)
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

# on button click, deletes the appropriate entry
# ****VERY BUGGY, BARELY WORKS****
def delete_entry(i):
    
    f = open("userinfo.txt", "r")
    for line in f:
        alist = line.split(',')
        print(alist)
        print(alist[0])
        print("i", i)
        if str(i) == alist[0]:
            replace_line("userinfo.txt", i, "")
            update_info()
        
# when "edit" is clicked, creates "delete" buttons next to each entry
def edit_entry():
    count = get_count()
    
    for i in range(count):
        delete = tk.Button(root, text= "X", fg = "red", command = partial(delete_entry, i))
        delete.grid(row = (4 + int(i)), column = 4)


def update_info():
    f = open("userinfo.txt", "r")
    for line in f:
        alist = line.split(',')
        name = alist[1]
        user = alist[2]
        password = alist[3]
        add_new(name, user, password)


# reads the userinfo from the text file and displays it on 
# the correct labels
def get_info_from_file():
    user_info = open("userinfo.txt", "r")
    
    count = 0
    for line in user_info:
        alist = line.split(',')
        name = alist[1]
        user = alist[2]
        password = alist[3]
        add_info(name, user, password, count)
        count +=1
        # print("alist", alist)

# when user clicks "Submit", userinfo is written to a text file and
# the userinfo entered is displayed
def on_submit():
    count = get_count()
    user_info = open("userinfo.txt","a")
    name = name_e.get()
    user = user_e.get()
    password = pass_e.get()
    user_info.write(str(count) + "," + name + "," + user + "," + password + ",\n" )
    add_new(name, user, password)
    name_e.delete(0, "end")
    user_e.delete(0, "end")
    pass_e.delete(0, "end")
    
    # tk.messagebox.showinfo('Success!','Successfully Added, \n' + 'Name: ' + name + '\nUser: ' + user + '\nPassword: ' + password)
	


######Graphics######
# number graphic attributes
number_label = tk.Label(root, width = LABEL_WIDTH, text = "Entry No.:")
number_label.grid(row = 3, column = 0)

# name graphic attributes
name_e = tk.Entry(root, width = ENTRY_WIDTH)
name = tk.StringVar()
name_label = tk.Label(root, width = LABEL_WIDTH, text = "Names:")
name_e.grid(row = 0, columnspan = 3, pady = 2)
name_label.grid(row = 3, column = 1, pady = 2)

# user graphic attributes
user_e = tk.Entry(root, width = ENTRY_WIDTH)
user = tk.StringVar()
user_label = tk.Label(root, width = LABEL_WIDTH, text = "Usernames:")
user_e.grid(row = 1, columnspan = 3, pady = 2)
user_label.grid(row = 3, column = 2, pady = 2)

# password graphic attributes
pass_e = tk.Entry(root, width = ENTRY_WIDTH)
password = tk.StringVar()
pass_label = tk.Label(root, width = LABEL_WIDTH, text = "Passwords:")
pass_e.grid(row  = 2, columnspan = 3, pady = 2)
pass_label.grid(row = 3, column = 3, pady = 2)

# submit button graphic attributes
submit_button = tk.Button(root, font = 40, text = "Submit", bg = "gray", command= on_submit)
submit_button.grid(row = 1, column= 2, pady = 2)	

# delete button graphic attributes
edit_button = tk.Button(root, text = "Edit", fg = "red", command = edit_entry)
edit_button.grid(row= 2, column = 2)


####################

get_info_from_file()
    
root.mainloop()
	

