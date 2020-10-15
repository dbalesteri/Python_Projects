#   Python: 3.9.0
#
#   Author: Dan S. Balesteri
#
#   Purpose: The Tech Academy - Python Course
#       page 171
#
# For this assignment, you will need to write a
# script that creates a database and adds new data into
# that database.
#
# Your database will require 2 fields: an auto-increment
# primary integer field and a field with the data type "string".
#
# Your script will need to read from the supplied list of file
# names at the bottom of this page and determine only the files
# from the list which end with a “.txt” file extension.
#
# Next, your script should add those file names from the list
# ending with “.txt” file extension within your database.
#
# Finally, your script should legibly print the qualifying text
# files to the console.
#

import sqlite3

conn = sqlite3.connect('assignment.db')

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileName STRING \
        )")
    conn.commit()

with conn:
    cur = conn.cursor()
    for i in fileList:
        if ".txt" in i:
            cur.execute("INSERT INTO tbl_fileList(col_fileName) VALUES(?)", \
                ('{}'.format(i),))
            print(i)
    conn.commit()
conn.close()
