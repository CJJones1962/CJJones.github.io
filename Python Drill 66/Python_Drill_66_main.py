from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import filedialog
from tkinter.filedialog import askdirectory
from datetime import datetime, timedelta
import Python_Drill_66_gui
import Python_Drill_66_func
from Python_Drill_66_func import copyFile
import Python_Drill_64

conn = sqlite3.connect('Movies.db')
c = conn.cursor()

def create_db(): ##create database function
    conn = sqlite3.connect('db_Movies.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_movies( \
            idColumn INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_Time TEXT\
            );")
        conn.commit()
    conn.close()

def updateDb():
    conn = sqlite3.connect('db_Movies.db')
    c = conn.cursor()

    c.execute("INSERT INTO tbl_movies(col_Time) VALUES (?)", (str(datetime.now()),)) #passing in one value letting it auto increment

    conn.commit()
    conn.close()

def readDb():  ##where ever it is you are doing your entry.set you need to pass this function into it // found it and did so
    conn = sqlite3.connect('db_Movies.db')
    c = conn.cursor()

    lastRunTime = c.execute("SELECT col_Time FROM tbl_movies WHERE idColumn = (SELECT MAX(idColumn) FROM tbl_movies)").fetchone()

    if lastRunTime == None:  ## this if statement replaces your old first_run function
        conn.close()
        return ("No previous data")

    conn.close()
    properLookingTime = lastRunTime[0].split(".") ##this removes everything after the decimal in the number returned for time
    return properLookingTime[0]

class ParentWindow(Frame):

    
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize (900,600) #(Height, Width)
        self.master.maxsize (900,600)

        Python_Drill_66_func.center_window(self,800,500)
        self.master.title("End Of Day Transfer")
        self.master.configure(bg="#F0F0F0")
    
        self.master.protocol("WM_DELETE_WINDOW", lambda: Python_Drill_66_func.ask_quit(self))
        arg = self.master
        self.source_entry = StringVar()
        self.destination_entry = StringVar()
##        self.filecheck_entry=StringVar()
##        self.filechecktime_entry=StringVar()
        self.readDb_entry = StringVar()
        self.readDb_entry.set(readDb())
        
        self.lbl_choose = tk.Label(self.master,text='Choose Folder and Click Run.')
        self.lbl_choose.grid(row=0,column=2,padx=(45,0),pady=(10,0),sticky= N+E)

    
        self.lbl_source = tk.Label(self.master,text='Source')
        self.lbl_source.grid(row=3,column=0,padx=(25,0),pady=(45,10),sticky= N+W)
        
        self.lbl_destination = tk.Label(self.master,text='Destination')
        self.lbl_destination.grid(row=5,column=0,padx=(25,0),pady=(45,10),sticky= N+W)
        
        self.lbl_execute = tk.Label(self.master,text='Execute')
        self.lbl_execute.grid(row=8,column=0,padx=(25,0),pady=(45,10),sticky= N+W)
        
        self.lbl_filecheck = tk.Label(self.master,text = 'File Check')
        self.lbl_filecheck.grid(row=6,column=0,padx=(25,0),pady=(45,10),sticky = N+W)

        self.lbl_filechecktime = tk.Label (self.master,text = 'Last File Check')
        self.lbl_filechecktime.grid(row=7,column=0,padx=(25,0),pady=(45,10),sticky = N+W)
        

        self.txt_choose_source = tk.Entry(self.master,textvariable=self.source_entry)
        self.txt_choose_source.grid(row=3,column=2,rowspan=2,columnspan=1,padx=(25,0),pady=(45,10),sticky=N+E+W)
    
        self.txt_choose_destination = tk.Entry(self.master,textvariable=self.destination_entry)
        self.txt_choose_destination.grid(row=5,column=2,rowspan=2,columnspan=1,padx=(25,0),pady=(45,10),sticky=N+E+W)

##        self.txt_filecheck = tk.Entry(self.master,textvariable=self.filecheck_entry)
##        self.txt_filecheck.grid(row=6,column=2,rowspan=4,columnspan=1,padx=(25,0),pady=(45,10),sticky=N+E+W)

        self.txt_filechecktime= tk.Entry(self.master,textvariable=self.readDb_entry) ##Changed this textvariable=self.readDb_entry
        self.txt_filechecktime.grid(row=7,column=2,rowspan=5, columnspan=1,padx=(25,0),pady=(45,10),sticky=N+E+W)
        
                    
        self.btn_choosefolder = tk.Button(self.master,width=12,text='Choose Folder',command=self.getSource)
        self.btn_choosefolder.grid(row=3,column=3,padx=(25,0),pady=(45,10),sticky = E)
        
        self.btn_choosefolder = tk.Button(self.master,width=12,text='Choose Folder',command=self.getDestination)
        self.btn_choosefolder.grid(row=5, column=3,padx=(25,0),pady=(45,10),sticky = E)
        
        self.btn_run = tk.Button(self.master,width=12,text='Run',command=self.move_file)
        self.btn_run.grid(row=8,column=18,padx=(25,0),pady=(45,10),sticky = E)
        
        self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: Python_Drill_66_func.ask_quit(self))
        self.btn_close.grid(row=10,column=18,padx=(10,0),pady=(35,10),sticky=E)


    def getSource (self):
        source = askdirectory()
        self.source_entry.set(source)

    def getDestination (self):
        destination = askdirectory()
        self.destination_entry.set (destination)

    def move_file(self):
        source = self.source_entry.get() + '/'
        destination = self.destination_entry.get() + '/'
        Python_Drill_66_func.copyFile(source,destination)
##        self.filecheck_entry.set(destination)
        updateDb()
        self.readDb_entry.set(readDb()) ## here is that passing the function into the .set
        

##    def filechecktime(self): #seem to be attempting to circumvent the table here
##        datetime.now = now()
##        Python_Drill_66func.copyFile(destination)
##        self.filechecktime_entry.set(now)                
##
##        Python_Drill_66_gui.load_gui(self)
##        Python_Drill_66_func.create_db(self)
##        
    
    
def main():
    create_db()
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()    
    



if __name__ == "__main__": main()  ##changed this to just call the main function, cleaner
