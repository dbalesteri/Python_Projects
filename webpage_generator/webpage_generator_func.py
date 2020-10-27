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
import webpage_generator_main


def createFile(self):
    fileName = self.txt_fileName.get()
    content = self.txt_body.get("1.0",'end-1c') #get all info from Text widget
    content = content.replace("\n","<br/>") #to ensure new lines translate to html body
    if (len(fileName) > 0): #ensure file name exists for creation
        htmlFile = open("{}.html".format(fileName),"w") #format as html file
        htmlFile.write("<html> \
     <body> \
	{}\
     </body> \
</html>".format(content)) #write to file as body
        htmlFile.close() #close file when finished
        askopen = messagebox.askokcancel("Open Now?","Your file: '{}' has been created. \n\nDo you wish to open it now?".format(fileName+".html"))
        if askopen: #if yes to open prompt, open file, otherwise back to main program
            openFile(fileName)
    else:
         messagebox.showerror("Missing Text","Please provide a valid file name. Web content can be blank.")

def openFile(fileName): #open file if desired
    webbrowser.open_new_tab("file://" + os.path.abspath(fileName+".html"))

def ask_quit(self): #double check if want to quit
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        #close app
        self.master.destroy()
        os.exit(0) 

if __name__ == "__main__":
    pass
    
