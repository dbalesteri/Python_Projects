#   Python: 3.9.0
#
#   Author: Dan S. Balesteri
#
#   Purpose: The Tech Academy - Python Course
#       Page 167 Assignment
#       For this assignment, you will need to write
#       a script that will check a specific folder on
#       the hard drive, verify whether those files end
#       with a “.txt” file extension and, if they do,
#       print those qualifying file names and their
#       corresponding modified time-stamps to the console.
#
#
#

import os
import time

def getFolder():
    folderName = input("\nWhich folder in the C: drive\nwould you like to search?\nFolder name must be exact!\n\n>>>:")
    if folderName == "":
        print("Please write a file name, cannot be left blank")
        getFolder()
    return folderName

folder = getFolder()

folderPath = "C:\\" + folder

dirList = os.listdir(folderPath)


if __name__ == "__main__":
    
    for i in dirList:
        if ".txt" in i:
            abPath = os.path.join(folderPath, i)
            mTime = os.path.getmtime(abPath)
            convertedTime = time.ctime(mTime)
            mTimeStr = str(convertedTime)
            print(i + " " + mTimeStr)
    
