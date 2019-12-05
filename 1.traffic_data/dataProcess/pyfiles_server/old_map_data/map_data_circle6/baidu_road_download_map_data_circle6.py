# -*- coding: utf-8 -*-

import urllib2
from PIL import Image
import cStringIO
import matplotlib.pyplot as plt
import datetime
import numpy as np
import math
import h5py
import matplotlib.image as mpimg
import random
import time

import os


def showBmap(my_url):
	file = cStringIO.StringIO(urllib2.urlopen(my_url).read())
	try:
		img = Image.open(file)
		img = img.convert("RGB")
	except IOError:
		return np.zeros((size,size))
	return img

def down_a_map(time_now):

	start_x = 3170
	start_y = 1186
	level = 14    
    
	size = 256
	x_range = 14
	y_range = 14
	tile_x =np.arange(start_x - x_range,start_x  , 1)
	tile_y =np.arange(start_y - y_range,start_y ,  1)
	myMap = np.zeros((len(tile_y)*size,len(tile_x)*size,3),dtype = 'uint8' )  
	address = 'http://its.map.baidu.com:8002/traffic/TrafficTileService?'#level=13&x=1580&y=589&time=1507687074027&v=081&smallflow=1&scaler=1
	
	for i in range(len(tile_x)):
		#print i
		for j in range(len(tile_y)):
			#print(i,j)
			#url_ij = address+('x=%d&y=%d&z=%d')%(tile_x[i],tile_y[j],level)
			url_ij = address+('level=%d&x=%d&y=%d&time=%d')%(level,tile_x[i],tile_y[j],time_now)
			#print(url_ij)
			temp = showBmap(url_ij)
			if temp.size == 65536:
				temp_3 =np.zeros((256,256,3))
				temp_3[:,:,0] = temp
				temp_3[:,:,1] = temp
				temp_3[:,:,2] = temp
				temp = temp_3
			myMap[ (y_range-j-1)*size:(y_range-j)*size ,i*size:(i+1)*size   ,: ] = np.array(temp)
			#plt.imshow(np.array(temp))
			#plt.imshow(myMap)
	return myMap


#import warnings
#warnings.filterwarnings('ignore')


size = 256
address = 'http://its.map.baidu.com:8002/traffic/TrafficTileService?'#level=13&x=1580&y=589&time=1507687074027&v=081&smallflow=1&scaler=1

time_now = int(time.time())
time_local = time.localtime(time_now)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

import string
dt_new = dt.replace(' ','_' )
dt_new = dt_new.replace(':','-' )
#print dt_new
#zhuanhuan cheng shijian shuzu
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#zhuanhuan cheng shijian chuo
timestamp = time.mktime(timeArray)
timestamp = timestamp *1000
ss = down_a_map(timestamp)
#file_name = time.asctime(time.localtime(timestamp/1000))
#plt.imshow(ss)
file_name = dt_new
plt.imsave(file_name+'.png',ss)
#print dt



