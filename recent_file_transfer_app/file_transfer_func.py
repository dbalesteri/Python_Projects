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

import os, shutil, sqlite3
from tkinter import *
from tkinter import messagebox, filedialog
import tkinter as tk
import time

# import other module
import file_transfer_main
import file_transfer_gui

def browseFile1(self):
    directory = filedialog.askdirectory()
    self.txt_file1.delete(0,END) #clear current contents to replace with new selection
    self.txt_file1.insert(END,directory) #populate entry with directory

def browseFile2(self):
    directory = filedialog.askdirectory()
    self.txt_file2.delete(0,END) #clear current contents to replace with new selection
    self.txt_file2.insert(END,directory) #populate entry with directory

def transferFiles(self):
    self.lbl_success.config(text="") #reset success label in-case doesn't work subsequent times
    source = self.txt_file1.get()
    destination = self.txt_file2.get()
    if (len(source) > 0) and (len(destination) > 0): #make sure both fields have been selected
        if source != destination:
            source = source + "/" #finish file path once data exists
            destination = destination + "/" #finish file path once data exists
            files = os.listdir(source)
            fileNames = "" #create list of files available to move
            for i in files:
                if checkModTime(source,i): #if clears checkModTime, add to file list available to move
                    fileNames = fileNames + i + "\n"
            if (len(fileNames) > 0):
                askToMove = messagebox.askokcancel("Ok to move?","Files available to move:\n\n{}\nDo you wish to continue?".format(fileNames))
                if askToMove:
                    for i in files:
                        if checkModTime(source,i):
                            shutil.move(source+i, destination)
                    self.lbl_success.config(text="File transfer success")
            else:
                messagebox.showerror("No targets","No files currently modified less than 24 hours ago in source folder.")
                self.lbl_success.config(text="No applicable files in folder")
        else:
            messagebox.showerror("Identical folders","Please provide two separate folders for source and destination.")
            self.lbl_success.config(text="Identical folders chosen")
    else:
        messagebox.showerror("Missing selection","Please ensure a folder is selected in both fields.")
        self.lbl_success.config(text="Missing folder selection")

def checkModTime(source,file):
    path = source + file #full file path
    modTime = os.path.getmtime(path) #file modification time
    curTime = time.time() #current time
    if (curTime - modTime) / 3600 < 24: #check to see if modified less than 24 hours ago
        return True
    else:
        return False

def ask_quit(self): #double check if want to quit
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #close app
        self.master.destroy()
        os.exit(0) 

if __name__ == "__main__":
    pass    
