# Dan Balesteri - Python 3.9.0 - Windows 10
#
# Web Page Generator Assignment - The Tech Academy
#
# Your task is to create a GUI with Tkinter that will enable
# the users to set the body text for a newly-created web page.
# There should also be a control in the GUI that initiates the
# process of making the new web page.
#
# Set a new body text of your choice.
#
# The GUI should open the html file in a new tab within your
# browser that displays the newly added text from the user.


import os, webbrowser, os.path
from tkinter import *
from tkinter import messagebox
import tkinter as tk

# import other module
import webpage_generator_main
import webpage_generator_func

def load_gui(self):

    self.lbl_title = tk.Label(self.master, text="Create a webpage!", font=('TkDefaultFont',20))
    self.lbl_title.grid(row=0,column=1,padx=(10,10),pady=(20,10),sticky=W)

    self.lbl_fileName = tk.Label(self.master, text="Enter desired file name (omit extention):")
    self.lbl_fileName.grid(row=1,column=0,padx=(20,10),pady=(0,0),sticky=W)

    self.txt_fileName = tk.Entry(self.master, text="", width=40)
    self.txt_fileName.grid(row=1, column=1, columnspan=2, padx=(20,10),pady=(10,10),sticky=W)
    
    self.lbl_instruction = tk.Label(self.master, text="Enter desired body text below:")
    self.lbl_instruction.grid(row=3,column=0,padx=(20,10),pady=(0,0),sticky=W)

    self.txt_body = tk.Text(self.master) #used Text() widget for multi line entry instead of Entry
    self.txt_body.grid(row=4, column=0, columnspan=3, padx=(20,10),pady=(10,10),sticky=W)

    self.btn_create = tk.Button(self.master,width=16,height=2,text="Create Webpage!",command=lambda: webpage_generator_func.createFile(self))
    self.btn_create.grid(row=5,column=0,padx=(60,10),pady=(10,10),sticky=W)

    self.btn_close = tk.Button(self.master,width=16,height=2,text="Close Program",command=lambda: webpage_generator_func.ask_quit(self))
    self.btn_close.grid(row=5,column=2,padx=(10,60),pady=(10,10),sticky=E)

    

if __name__ == "__main__":
    pass
