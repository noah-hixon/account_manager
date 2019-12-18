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


# takes userinfo from entry boxes and displays it
def add_info(result_name, result_user, result_pass):

	result_name = name_e.get()
	new_name = name_l.cget("text") + result_name
	name.set(new_name + "\n")

	result_user = user_e.get()
	new_user = user_l.cget("text") + result_user
	user.set(new_user + "\n")

	result_pass = pass_e.get()
	new_pass = pass_l.cget("text") + result_pass
	password.set(new_pass + "\n")


# takes the userinfo from get_info_from_file and displays it
def add_from_file(result_name, result_user, result_pass):
	new_name = name_l.cget("text") + result_name
	name.set(new_name + "\n")

	new_user = user_l.cget("text") + result_user
	user.set(new_user + "\n")
	
	new_pass = pass_l.cget("text") + result_pass
	password.set(new_pass + "\n")
	
	print("results", result_name, result_user, result_pass)

	

# reads the userinfo from the text file and displays it on 
# the correct labels
def get_info_from_file():
	user_info = open("userinfo.txt", "r")
	user_info.readline()
	for line in user_info:
		alist = line.split(',')
		name = alist[0]
		user = alist[1]
		password = alist[2]
		add_from_file(name, user, password)
		
		print(name, user, password)
	


# when user clicks "Submit", userinfo is written to a text file and
# the userinfo entered is displayed
def on_submit():
	
	user_info = open("userinfo.txt","a")
	name = name_e.get()
	user = user_e.get()
	password = pass_e.get()
	#add_info(name, user, password)
	user_info.write(name + "," + user + "," + password + ",\n" )
	add_info(name, user, password)	
	name_e.delete(0, "end")
	user_e.delete(0, "end")
	pass_e.delete(0, "end")
	

	tk.messagebox.showinfo('Success!','Successfully Added, \n' + 'Name: ' + name + '\nUser: ' + user + '\nPassword: ' + password)
	


######Graphics######

# name graphic attributes
name_e = tk.Entry(root, width = ENTRY_WIDTH)
name = tk.StringVar()
name_l = tk.Label(root, width = LABEL_WIDTH, textvariable = name, relief = "raised", bg = "lightgray")
name_display = tk.Label(root, width = LABEL_WIDTH, text = "Names:")
name_e.grid(row = 0, columnspan = 3, pady = 2)
name_l.grid(row = 4, column = 0, pady = 2)
name_display.grid(row = 3, column = 0, pady = 2)

# user graphic attributes
user_e = tk.Entry(root, width = ENTRY_WIDTH)
user = tk.StringVar()
user_l = tk.Label(root, width = LABEL_WIDTH, textvariable = user, relief = "raised", bg = "lightgray")
user_display = tk.Label(root, width = LABEL_WIDTH, text = "Usernames:")
user_e.grid(row = 1, columnspan = 3, pady = 2)
user_l.grid(row = 4, column = 1, pady = 2)
user_display.grid(row = 3, column = 1, pady = 2)

# password graphic attributes
pass_e = tk.Entry(root, width = ENTRY_WIDTH)
password = tk.StringVar()
pass_l = tk.Label(root, width = LABEL_WIDTH, textvariable = password, relief = "raised", bg = "lightgray")
pass_display = tk.Label(root, width = LABEL_WIDTH, text = "Passwords:")
pass_e.grid(row  = 2, columnspan = 3, pady = 2)
pass_l.grid(row = 4, column = 2, pady = 2)
pass_display.grid(row = 3, column = 2, pady = 2)



# button graphic attributes
button = tk.Button(root, font = 40, text = "Submit", bg = "gray", command= on_submit)
button.grid(row = 1, column= 2, pady = 2)	

####################

get_info_from_file()
	
root.mainloop()
	

