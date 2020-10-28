# Dan Balesteri - Python 3.9.0 - Windows 10
#
# FILE TRANSFER ASSIGNMENT - The Tech Academy
#
# Once per day, any files that are new, or that
# were edited within the previous 24 hours, must be
# sent to the home office. To facilitate this, these new
# or updated files need to be copied to a specific
# 'destination' folder on a computer so that a special
# file transfer program can grab them and transfer them
# to the home office.
#
# Allow the user to browse and choose a specific
# folder that will contain the files to be checked daily.
#
# Allow the user to browse and choose a specific folder
# that will receive the copied files.
#
# Allow the user to manually initiate the 'file check'
# process that is performed by the script.


import os, shutil
from tkinter import *
import tkinter as tk
from tkinter import messagebox

#Other modules import
import file_transfer_gui
import file_transfer_func

#Frame is Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        self.master = master
        self.master.minsize(540,220) #(Wpx,Hpx)
        self.master.maxsize(540,220)
        self.master.configure(bg="#F0F0F0")
        arg = self.master

        #load in GUI widgets from separate module
        file_transfer_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk() #create window from tkinter
    App = ParentWindow(root) # pass root into our class
    root.mainloop() #persistence on screen
