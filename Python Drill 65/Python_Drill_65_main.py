from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askdirectory


import Python_Drill_65_gui
import Python_Drill_65_func
from Python_Drill_65_func import copyFile
import Python_Drill_64


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize (600,400) #(Height, Width)
        self.master.maxsize (600,400)

        Python_Drill_65_func.center_window(self,600,400)
        self.master.title("End Of Day Transfer")
        self.master.configure(bg="#F0F0F0")
    
        self.master.protocol("WM_DELETE_WINDOW", lambda: Python_Drill_65_func.ask_quit(self))
        arg = self.master
        self.source_entry = StringVar()
        self.destination_entry = StringVar()
        self.lbl_choose = tk.Label(self.master,text='Choose Folder and Click Run.')
        self.lbl_choose.grid(row=0,column=2,padx=(45,0),pady=(10,0),sticky= N+E)
    ##CHANGES
##    self.lbl_choosefolder = tk.Label(self.master,width=12,text='Choose Folder')
##    self.lbl_choosefolder.grid(row=3,column=3,padx=(25,0),pady=(45,10),sticky = E)
##    self.lbl_choosefolder = tk.Label(self.master,width=12,text='Choose Folder')
##    self.lbl_choosefolder.grid(row=5,column=3,padx=(25,0),pady=(45,10),sticky = E)
    
        self.lbl_source = tk.Label(self.master,text='Source')
        self.lbl_source.grid(row=3,column=0,padx=(25,0),pady=(45,10),sticky= N+W)
        self.lbl_destination = tk.Label(self.master,text='Destination')
        self.lbl_destination.grid(row=5,column=0,padx=(25,0),pady=(45,10),sticky= N+W)
        self.lbl_execute = tk.Label(self.master,text='Execute')
        self.lbl_execute.grid(row=6,column=0,padx=(25,0),pady=(45,10),sticky= N+W)
##CHANGES
        self.txt_choose_source = tk.Entry(self.master,textvariable=self.source_entry)
        self.txt_choose_source.grid(row=3,column=2,rowspan=2,columnspan=1,padx=(25,0),pady=(45,10),sticky=N+E+W)
    
        self.txt_choose_destination = tk.Entry(self.master,textvariable=self.destination_entry)
        self.txt_choose_destination.grid(row=5,column=2,rowspan=2,columnspan=1,padx=(25,0),pady=(45,10),sticky=N+E+W)
    
    
        self.btn_choosefolder = tk.Button(self.master,width=12,text='Choose Folder',command=self.getSource)
        self.btn_choosefolder.grid(row=3,column=3,padx=(25,0),pady=(45,10),sticky = E)
        self.btn_choosefolder = tk.Button(self.master,width=12,text='Choose Folder',command=self.getDestination)
        self.btn_choosefolder.grid(row=5, column=3,padx=(25,0),pady=(45,10),sticky = E)
        self.btn_run = tk.Button(self.master,width=12,text='Run',command=self.move_file)
        self.btn_run.grid(row=6,column=4,padx=(25,0),pady=(45,10),sticky = E)
        self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: Python_Drill_65_func.ask_quit(self))
        self.btn_close.grid(row=7,column=4,padx=(10,0),pady=(35,10),sticky=E)

    def getSource (self):
        source = askdirectory()
        self.source_entry.set(source)

    def getDestination (self):
        destination = askdirectory()
        self.destination_entry.set (destination)

    def move_file(self):
        source = self.source_entry.get() + '/'
        destination = self.destination_entry.get() + '/'
        copyFile(source,destination)

        Python_Drill_65_gui.load_gui(self)
    
    
    
    



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
