# delete datas in tempdata dirs based on ubuntu server

import os
import shutil
import sys

rootDirPath = os.getcwd()
folderName = []
tempdatadir = ['tempdata', 'tempdata1', 'tempdata2']


# define func let int transto two chars like 0 --> '00'
def number_to_twochars(time_num):
    twocharsstr = time_num
    twocharsstr = str(time_num)
    twocharsstr = twocharsstr.zfill(2)
    return twocharsstr

yearstr = sys.argv[1]
monthstr = sys.argv[2]
daystr = sys.argv[3]
datestr = ""
datestr = yearstr+'-'+monthstr+'-'+daystr
print(datestr)

for tempdir in tempdatadir:
	dirnow = rootDirPath + '/' + tempdir
	for data in os.listdir(dirnow):
		if(data.split('_')[0] == datestr):
			datapath = dirnow +'/' + data
			os.remove(datapath)
			




