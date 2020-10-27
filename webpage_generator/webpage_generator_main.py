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
import tkinter as tk
from tkinter import messagebox

#Other modules import
import webpage_generator_gui
import webpage_generator_func

#Frame is Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define master gui frame size
        self.master = master
        self.master.minsize(700,500) #(Wpx,Hpx)
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        #load in GUI widgets from separate module
        webpage_generator_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk() #create window from tkinter
    App = ParentWindow(root) # pass root into our class
    root.mainloop() #persistence on screen
