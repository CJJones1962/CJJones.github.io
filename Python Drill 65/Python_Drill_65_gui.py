from tkinter import *
import tkinter as tk


import Python_Drill_65_main
import Python_Drill_65_func
import Python_Drill_64

def load_gui(self):
##CHANGES
    
    
    ##CHANGES
    def source_function(self):
        source = askdirectory()
        self.choose_src.set(source)

##Start with this
    def destination_function(self):
        destination = askdirectory()
        self.choose_des.set(destination)
        
    def move_file():
        source = self.choose_src.get() + '/'
        fileTime = ('%H:') ##This and the 'files' variable I'm just going off of your functions file,
        ##if you have set them to something else in this then use that
        destination = self.choose_des.get() + '/'
        files = os.listdir(source)
        copyFile(source, destination)
        ##your files should be moved once you do the same process for setting the destination variable
                          
##    Python_Drill_65_func.create_db(self)
##    Python_Drill_65_func.onRefresh(self)

if __name__ == "__main__":
    pass
