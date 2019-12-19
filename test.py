###################
# Account Manager #
###################

import tkinter as tk
from tkinter import messagebox
import tkinter.messagebox

### Constants ###
HEIGHT = 700
WIDTH = 800
ENTRY_WIDTH = 25
LABEL_WIDTH = 25
root = tk.Tk()
root.title("Account Manager")
root.geometry("+400+200")
users = []



#################



# adds userinfo to appropriate label with delete button
# *From File*
def add_info(name, user, password, count):
    name_display = tk.Label(root, text = str(count + 1) + ". " + name)
    user_display = tk.Label(root, text = user)
    pass_display = tk.Label(root, text = password)
    delete_button = tk.Button(root, text = "X",fg = "red", command = delete_entry)

    delete_button.grid(row = (4 + count), column  = 3)
    name_display.grid(row = (4 + count), column = 0)
    user_display.grid(row = (4 + count), column = 1)
    pass_display.grid(row = (4 + count), column = 2)

# adds userinfo to appropriate label with delete button
# *From Entry*
def add_new(name, user, password):
    f = open("userinfo.txt", "r")
    count = 0
    for line in f:
        count += 1
    
    name_display = tk.Label(root, text = str(count) + ". "  + name)
    user_display = tk.Label(root, text = user)
    pass_display = tk.Label(root, text = password)
    delete_button = tk.Button(root, text = "X",fg = "red",command = delete_entry)

    delete_button.grid(row = (4 + count), column  = 3)
    name_display.grid(row = (4 + count), column = 0)
    user_display.grid(row = (4 + count), column = 1)
    pass_display.grid(row = (4 + count), column = 2)


def on_delete_submit():
    f = open("userinfo.txt", "r")

    count = 0
    user_list = []
    for line in f:
        e = delete_e.get()
        
        alist = line.split(',')
        name = alist[0]
        user = alist[1]
        password = alist[2]
        
        user_list.append(str(count) + name + user + password)
        print(user_list)
        # print("names:", user_list[count][1])
        
        if e == user_list[count][0]:
            print("HERE")
        
        
        
        count += 1
    print("here")
    
# displays a new window when the user wants to delete an entry
def delete_display():
    delete = tk.Tk()
    delete.title("Delete Entry")
    delete.geometry("+200+400")
    
    global delete_e
    delete_e = tk.Entry(delete, width = 40) 
    delete_question = tk.Label(delete, font = 30, text = "What entry to do want to delete?")
    delete_submit = tk.Button(delete, text = "Submit", command = on_delete_submit)

    delete_submit.pack()
    delete_question.pack()
    delete_e.pack()
    delete.mainloop()


# on button click, a window pops up asking
# the user which entry they want to delete ***DOESN'T DO ANYTHING YET***
def delete_entry():
    user_info = open("userinfo.txt", "r")
    user_info.readline()
    count = 0
    user_list = []
    for line in user_info:
        
        alist = line.split(',')
        name = alist[0]
        user = alist[1]
        password = alist[2]
        
        user_list.append(str(count) + name + user + password)
        
        # print("names:", user_list[count][1])
        count += 1
    
    delete_display()
    print(user_list)


# reads the userinfo from the text file and displays it on 
# the correct labels
def get_info_from_file():
    user_info = open("userinfo.txt", "r")
    user_info.readline()
    count = 0
    for line in user_info:
        
        alist = line.split(',')
        name = alist[0]
        user = alist[1]
        password = alist[2]
        add_info(name, user, password, count)
        count +=1


# when user clicks "Submit", userinfo is written to a text file and
# the userinfo entered is displayed
def on_submit():
    
    user_info = open("userinfo.txt","a")
    name = name_e.get()
    user = user_e.get()
    password = pass_e.get()
    user_info.write(name + "," + user + "," + password + ",\n" )
    # add_info(name, user, password, count)
    # print("count:", count)
    add_new(name, user, password)
    name_e.delete(0, "end")
    user_e.delete(0, "end")
    pass_e.delete(0, "end")
    
    tk.messagebox.showinfo('Success!','Successfully Added, \n' + 'Name: ' + name + '\nUser: ' + user + '\nPassword: ' + password)
	


######Graphics######

# name graphic attributes
name_e = tk.Entry(root, width = ENTRY_WIDTH)
name = tk.StringVar()
# name_l = tk.Label(root, width = LABEL_WIDTH, textvariable = name, relief = "raised", bg = "lightgray")
name_display = tk.Label(root, width = LABEL_WIDTH, text = "Names:")
name_e.grid(row = 0, columnspan = 3, pady = 2)
# name_l.grid(row = 4, column = 0, pady = 2)
name_display.grid(row = 3, column = 0, pady = 2)

# user graphic attributes
user_e = tk.Entry(root, width = ENTRY_WIDTH)
user = tk.StringVar()
# user_l = tk.Label(root, width = LABEL_WIDTH, textvariable = user, relief = "raised", bg = "lightgray")
user_display = tk.Label(root, width = LABEL_WIDTH, text = "Usernames:")
user_e.grid(row = 1, columnspan = 3, pady = 2)
# user_l.grid(row = 4, column = 1, pady = 2)
user_display.grid(row = 3, column = 1, pady = 2)

# password graphic attributes
pass_e = tk.Entry(root, width = ENTRY_WIDTH)
password = tk.StringVar()
# pass_l = tk.Label(root, width = LABEL_WIDTH, textvariable = password, relief = "raised", bg = "lightgray")
pass_display = tk.Label(root, width = LABEL_WIDTH, text = "Passwords:")
pass_e.grid(row  = 2, columnspan = 3, pady = 2)
# pass_l.grid(row = 4, column = 2, pady = 2)
pass_display.grid(row = 3, column = 2, pady = 2)

# submit button graphic attributes
submit_button = tk.Button(root, font = 40, text = "Submit", bg = "gray", command= on_submit)
submit_button.grid(row = 1, column= 2, pady = 2)	

# delete button graphic attributes
# delete_button = tk.Button(root, text = "X", fg = "red", command = delete_entry)
# delete_button.grid(row= 2, column = 2)


####################

get_info_from_file()
	
root.mainloop()
	
