from tkinter import *
import tkinter as tk


import Python_Drill_66_main
import Python_Drill_66_func
import Python_Drill_64

def load_gui(self):

    
    
    
    def source_function(self):
        source = askdirectory()
        self.choose_src.set(source)


    def destination_function(self):
        destination = askdirectory()
        self.choose_des.set(destination)
        
    def move_file():
        source = self.choose_src.get() + '/'
        fileTime = ('%H:') 
        destination = self.choose_des.get() + '/'
        files = os.listdir(source)
        copyFile(source, destination)
        
                          
##    Python_Drill_66_func.create_db(self)
##    Python_Drill_66_func.onRefresh(self)

if __name__ == "__main__":
    pass
