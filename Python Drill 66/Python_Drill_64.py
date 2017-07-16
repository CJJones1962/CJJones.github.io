import shutil
import os
from shutil import copyfile
import time;
from datetime import datetime, timedelta


def start():
    copy_req = raw_input('\n Press C to copy your updated files.').capitalize()
    if copy_req == 'C':
        source =  "C:/Users/HP/Desktop/folderA/"
        files = os.listdir(source)
        destination =  "C:/Users/HP/Desktop/folderB/"
        fileTime = ('%H:')
        copyFile(source, fileTime, destination, files)
               
def copyFile(source, fileTime, destination, files):
    now = datetime.now()
    for file in files:
        if file.endswith(".txt"):
               fileCreation = (now - (datetime.fromtimestamp(os.path.getmtime(source + file))))
               print (fileCreation)
               if fileCreation < timedelta(days=1):
                 d = timedelta(seconds = -1)
                 (d.days, d.seconds,d.microseconds)
                 shutil.copy(source + file,destination + file)
                 if destination:   
                     print (destination + '\n Your modified files have been successfully copied.')
                 else:
                     print ('\nyou need to press C to copy your files. Try again please')
                     print (file)
if __name__ == '__main__':

    start()
