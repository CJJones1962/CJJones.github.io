import shutil
import os

def start():
    trans_req = raw_input('\n Press T to transfer your files.').capitalize()
    if trans_req == 'T':
        source =  "C:/Users/HP/Desktop/folderA/"
        sourceFiles = os.listdir(source)
        destination =  "C:/Users/HP/Desktop/folderB/"
        cleanUp(source, sourceFiles, destination)
    
def cleanUp(source, sourceFiles, destination):
    for file in sourceFiles:
        if file.endswith(".txt"):
             shutil.move(source + file,destination + file)
             print file
        if destination:   
            print (destination + '\nhas been transferred.')
            print ('\n Your files have been successfully transferred.')
        else:
             print ('\nyou need to press T to transfer your files. Try again please')
if __name__ == '__main__':

    start()
