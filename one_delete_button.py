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
ENTRY_WIDTH = 20
LABEL_WIDTH = 10
root = tk.Tk()
root.title("Account Manager")
root.geometry("+400+200")
users = []
#################

# gets the number of lines in the text file and returns it
def get_count():
    f = open("userinfo.txt", "r")
    count = 0
    for line in f:
        count += 1
    return count

# adds userinfo to appropriate label with delete button *From File*
def add_info(name, user, password, count):
    name_display = tk.Label(root, text = name)
    user_display = tk.Label(root, text = user)
    pass_display = tk.Label(root, text = password)

    name_display.grid(row = (4 + count), column = 0)
    user_display.grid(row = (4 + count), column = 1)
    pass_display.grid(row = (4 + count), column = 2)

# adds userinfo to appropriate label with delete button *From Entry*
def add_new(name, user, password):
    count = get_count()
    
    name_display = tk.Label(root, text = name)
    user_display = tk.Label(root, text = user)
    pass_display = tk.Label(root, text = password)
    
    name_display.grid(row = (4 + count), column = 0)
    user_display.grid(row = (4 + count), column = 1)
    pass_display.grid(row = (4 + count), column = 2)


# replaces the line in the file with an empty string(deletes it)
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    print(lines)
    print("Linenum", line_num)
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

# on button click, deletes the appropriate entry
def delete_entry(i):
    
    f = open("userinfo.txt", "r")
    for line in f:
        alist = line.split(',')
        
        # print(alist[0])
        # print("i", i)
        if str(i) == alist[0]:
            answer = tkinter.messagebox.askquestion('Delete', 'Are you sure you want to delete this entry?')
            if answer == "yes":
                replace_line("userinfo.txt", i, "")
                update_info()
        
# when "submit" is clicked, creates "delete" buttons next to each entry
def edit_entry():
    count = get_count()
    
    for i in range(count):
        delete = tk.Button(root, text= "X", fg = "red", command = partial(delete_entry, i))
        delete.grid(row = (4 + int(i)), column = 4)

# updates info after an edit ***doesn't work***
def update_info():
    f = open("userinfo.txt", "r")
    for line in f:
        alist = line.split(',')
        name = alist[1]
        user = alist[2]
        password = alist[3]
        add_new(name, user, password)


# reads the userinfo from the text file and displays it on the correct labels
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

# when user clicks "Submit", userinfo is written to a text file and the userinfo entered is displayed
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

# name graphic attributes
name_e = tk.Entry(root, width = ENTRY_WIDTH)
name = tk.StringVar()
name_label = tk.Label(root, width = LABEL_WIDTH, text = "Names:")
name_label2 = tk.Label(root, width = LABEL_WIDTH, text = "Name:", anchor = "e", font = ("Source Code Pro", 14))
name_e.grid(row = 0, column = 1, pady = 2)
name_label.grid(row = 3, column = 0, pady = 2)
name_label2.grid(row = 0, column = 0)

# user graphic attributes
user_e = tk.Entry(root, width = ENTRY_WIDTH)
user = tk.StringVar()
user_label = tk.Label(root, width = LABEL_WIDTH, text = "Usernames:")
user_label2 = tk.Label(root, width = LABEL_WIDTH, text = "Username:", anchor = "e", font = ("Source Code Pro", 14))
user_e.grid(row = 1, column = 1, pady = 2)
user_label.grid(row = 3, column = 1, pady = 2)
user_label2.grid(row = 1, column = 0)

# password graphic attributes
pass_e = tk.Entry(root, width = ENTRY_WIDTH, show = "*")
password = tk.StringVar()
pass_label = tk.Label(root, width = LABEL_WIDTH, text = "Passwords:")
pass_label2 = tk.Label(root, width = LABEL_WIDTH, text = "Password:", anchor = "e", font = ("Source Code Pro", 14))
pass_e.grid(row  = 2, column = 1, pady = 2)
pass_label.grid(row = 3, column = 2, pady = 2)
pass_label2.grid(row = 2, column = 0)
# submit button graphic attributes
submit_button = tk.Button(root, font = ("Source Code Pro", 10), text = "Submit", bg = "gray", command = lambda: [on_submit(), edit_entry()])
submit_button.grid(row = 1, column= 2, pady = 2)	

####################

get_info_from_file()
    
root.mainloop()
	

