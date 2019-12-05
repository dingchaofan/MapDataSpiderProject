import os
import shutil


rootDirPath = os.getcwd()
folderName = []
tempdatadirlist = ['tempdata', 'tempdata1', 'tempdata2']
tempdatadir = rootDirPath + '\\' + tempdatadirlist[0]

def file_name(file_dir): 
    for root, dirs, files in os.walk(file_dir):
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件


for filename in os.listdir(tempdatadir):
    data = filename.split(' ')[0]
    datadir = rootDirPath +'\\'+ data
    if(os.path.isdir(datadir)):
        filepath = tempdatadir + '\\' + filename
        shutil.move(filepath,datadir)
        print(filename + " is moved")
        
        
        
        