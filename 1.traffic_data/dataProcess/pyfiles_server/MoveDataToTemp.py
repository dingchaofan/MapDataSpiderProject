# move datas to tempdata dirs based on ubuntu server

import os
import shutil
import sys

rootDirPath = os.getcwd()
folderName = []
sourcedatadir = ['map_data_level14', 'map_data_level16', 'mapdata_level17']
tempdatadir = ['tempdata14', 'tempdata16', 'tempdata17']


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

for i in range(len(sourcedatadir)):
	sourcedirnow = rootDirPath + '/' + sourcedatadir[i]
	tempdirnow = rootDirPath + '/' + tempdatadir[i]
	for data in os.listdir(sourcedirnow):
		if(data.split('_')[0] == datestr):
			datapath = sourcedirnow + '/' + data
			shutil.move(datapath,tempdirnow)
			




