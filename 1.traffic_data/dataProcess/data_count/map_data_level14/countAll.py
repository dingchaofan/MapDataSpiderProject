import os
import shutil


def move_py_file():
	if(os.path.exists(pythonFliePath) == False and os.path.isdir(dirPath) == True):
		shutil.copy(src,dirPath)

folderNameList = []
src = "count_05.py"  #要复制的脚本名
rootDirPath = os.getcwd()
for file in os.listdir(rootDirPath):
	dirPath = rootDirPath + "\\" + file
	pythonFliePath = rootDirPath + "\\" + file + "\\" + src
	# move_py_file()
	if(os.path.exists(pythonFliePath) == True and len(os.listdir(dirPath)) > 100):
		os.chdir(dirPath)
		os.system("python count_05.py")
		os.remove(pythonFliePath)
		os.chdir(rootDirPath)