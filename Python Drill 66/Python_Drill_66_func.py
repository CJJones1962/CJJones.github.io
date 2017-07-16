import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox
import shutil
from shutil import copyfile
import time;
from datetime import datetime, timedelta
import tkinter.filedialog
from tkinter.filedialog import askdirectory



import Python_Drill_66_main
import Python_Drill_66_gui
import Python_Drill_64

def center_window(self,w,h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


##def create_db(self):
##    conn = sqlite3.connect('db_Movies.db')
##    with conn:
##        cur = conn.cursor()
##        cur.execute("CREATE TABLE if not exists tbl_movies( \
##            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
##            col_lname TEXT,\
##            col_fname TEXT,\
##            col_title TEXT\
##            );")
##        conn.commit()
##    conn.close()
##    first_run(self)

##def first_run(self):
##    conn = sqlite3.connect('db_Movies.db')
##    with conn:
##        cur = conn.cursor()
##        cur,count = count_records(cur)
##        if count < 1:
##            cur.execute("INSERT INTO tbl_movies (col_lname,col_fname,col_title)VALUES(?,?,?)",(datetime.now))
##
##def count_records(cur):
##    count = ""
##    cur.execute('SELECT COUNT(*) FROM tbl_movies')
##    count = cur.fetchone()[0]
##    return cur,count
##
##def finalCheckTime(self):
##    cur.execute("SELECT Time FROM time Tbl ORDER BY DESC Limit 1")
##    lastTime = c.fetchone()
##    self.LasTun.set(lastTime)


    
def start(self):
    copy_req = input('\n Press C to copy your updated files.').capitalize()
    if copy_req == 'C':
            files = os.listdir(source)
            fileTime = ('%H:')
            copyFile(source, fileTime, destination, files)
            
def Entrybox(askdirectory):
    theinput = inputbox.get()
    

def getSrource (self):
    source = askdirectory()
    self.source_entry.set(source)

def getDestination (self):
    destination = askdirectory()
    self.des_entry.set(destination)

def xfer(self):
    source = self.source_entry.get() +'/'
    destination = self.destination_entry.get() + '/'
    copyOver(source,destination)
       
    
def copyFile(source, destination):
    now = datetime.now()
    files = os.listdir(source)
    fileTime = ('%H:')
    for file in files:
        if file.endswith(".txt"):
               fileCreation = (now - (datetime.fromtimestamp(os.path.getmtime(source + file))))
               print (fileCreation)
               if fileCreation < timedelta(days=1):
                 d = timedelta(seconds = -1)
                 (d.days, d.seconds,d.microseconds)
                 shutil.copy(source + file,destination)
       
def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Okay to exit spplication?"):
        self.master.destroy()
        os._exit(0)
        
    else: confirm = messagebox.askokcancel()             

             


    
if __name__ == "__main__":
    pass
