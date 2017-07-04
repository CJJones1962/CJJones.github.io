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



import Python_Drill_65_main
import Python_Drill_65_gui
import Python_Drill_64

    
def start(self):
    copy_req = input('\n Press C to copy your updated files.').capitalize()
    if copy_req == 'C':
##            source =  "C:/Users/HP/Desktop/folderA/"
            files = os.listdir(source)
##            destination =  "C:/Users/HP/Desktop/folderB/"
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
       
##def chooseFolder(self):
##    self.source = filedialog.askdirectory()
##   source = "C:/Users/HP/Desktop/folderA/"
##    files = os.listdir(source)
##    destination = "C:/Users/HP/Desktop/folderB/"
    
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
                 
def center_window(self,w,h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Okay to exit spplication?"):
        self.master.destroy()
        os._exit(0)
        
    else: confirm = messagebox.askokcancel()
             
##class askdirectory:

    
if __name__ == "__main__":
    pass
