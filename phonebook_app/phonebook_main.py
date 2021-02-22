#Python Ver: 3.9.0
#
#Author: Dan S. Balesteri
#
#Purpose: Phonebook App, The Tech Academy Project
#           Demonstrating OOP, Tkinter GUI module,
#           using Tkinter Parent and Child relationships.
#
#Tested OS: This code was written and tested to work with Windows 10

from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Other modules import
import phonebook_gui
import phonebook_func

#Frame is Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Hpx,Wpx)
        self.master.maxsize(500,300)
        #CenterWindow method will center app on user's screen
        phonebook_func.center_window(self,500,300)
        self.master.configure(bg="#F0F0F0")
        #This protocol method is a tkinter built-in method to catch if
        #the user clicks the upper corner, "X", on Windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in GUI widgets from separate module,
        #keeping code compartmentalized & clutter free
        phonebook_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk() #required to create window from tkinter
    App = ParentWindow(root) # pass root into our class
    root.mainloop() #required to be persistent on screen
        
