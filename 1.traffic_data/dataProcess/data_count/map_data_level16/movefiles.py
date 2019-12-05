import os
import shutil


rootDirPath = os.getcwd()
folderName = []
tempdatadir = ['tempdata', 'tempdata1', 'tempdata2']


def file_name(file_dir): 
    for root, dirs, files in os.walk(file_dir):
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件

for dir in os.listdir(rootDirPath):
    print(dir)
    if os.path.isdir(dir):
        dirnow = rootDirPath + '\\' + dir
        if tempdatadir[0] in os.listdir(dirnow):
            print(tempdatadir[0] + ' exits')
            tempdata = dirnow + '\\' +tempdatadir[0]
            TempDataDirnow = dirnow.replace("map_partof16","map_data")
            for data in os.listdir(tempdata):
                data = tempdata + '\\' + data
                shutil.move(data,TempDataDirnow)
            os.rmdir(tempdata)
        if tempdatadir[1] in os.listdir(dirnow):
            print(tempdatadir[1] + ' exits')
            tempdata1 = dirnow + '\\' +tempdatadir[1]
            TempData1Dirnow = dirnow.replace("map_partof16","map_data_circle6")
            for data in os.listdir(tempdata1):    
                data = tempdata1 + '\\' + data
                shutil.move(data,TempData1Dirnow)
            os.rmdir(tempdata1)
        if tempdatadir[2] in os.listdir(dirnow):
            print(tempdatadir[2] + ' exits')
            tempdata2 = dirnow + '\\' +tempdatadir[2]
            TempData2Dirnow = dirnow
            for data in os.listdir(tempdata2):
                data = tempdata2 + '\\' + data
                shutil.move(data,TempData2Dirnow)
            os.rmdir(tempdata2)
        
        
        
        