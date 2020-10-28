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
from tkinter import messagebox
import tkinter as tk

# import other module
import file_transfer_main
import file_transfer_func

def load_gui(self):

    self.lbl_title = tk.Label(self.master, text="Transfer recent files", font=('TkDefaultFont',16))
    self.lbl_title.grid(row=0,column=1,padx=(0,0),pady=(20,10),sticky=W)

    self.lbl_source = tk.Label(self.master, text="Source Folder:")
    self.lbl_source.grid(row=1,column=0,padx=(10,10),pady=(0,0),sticky=W)
    self.lbl_destination = tk.Label(self.master, text="Destination Folder:")
    self.lbl_destination.grid(row=2,column=0,padx=(10,10),pady=(0,0),sticky=W)

    self.lbl_success = tk.Label(self.master, text="", font=('TkDefaultFont',14))
    self.lbl_success.grid(row=3,column=1,padx=(10,0),pady=(20,10),sticky=W)

    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text="Browse...",command=lambda: file_transfer_func.browseFile1(self))
    self.btn_browse1.grid(row=1,column=5,padx=(10,10),pady=(10,10),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text="Browse...",command=lambda: file_transfer_func.browseFile2(self))
    self.btn_browse2.grid(row=2,column=5,padx=(10,10),pady=(10,10),sticky=W)
    self.btn_check = tk.Button(self.master,width=18,height=2,text="Check for recent files...",command=lambda: file_transfer_func.transferFiles(self))
    self.btn_check.grid(row=3,column=0,padx=(10,10),pady=(10,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text="Close Program",command=lambda: file_transfer_func.ask_quit(self))
    self.btn_close.grid(row=3,column=5,padx=(10,10),pady=(10,10),sticky=E)

    self.txt_file1 = tk.Entry(self.master,text="",width=40)
    self.txt_file1.grid(row=1, column=1, columnspan=4, padx=(0,10),pady=(10,10))
    self.txt_file2 = tk.Entry(self.master,text="",width=40)
    self.txt_file2.grid(row=2, column=1, columnspan=4, padx=(0,10),pady=(10,10))

    

if __name__ == "__main__":
    pass
