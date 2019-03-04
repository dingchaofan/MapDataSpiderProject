# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:17:28 2017

@author: zhangqi
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:54:41 2017

@author: zhangqi
"""

import urllib2
from PIL import Image
import cStringIO
import matplotlib.pyplot as plt
import time
import datetime
import numpy as np
import math
import h5py
import matplotlib.image as mpimg # mpimg ç¨äºè¯»åå¾ç
import random
import time


def showBmap(my_url):
    file = cStringIO.StringIO(urllib2.urlopen(my_url).read())
    try:
        img = Image.open(file)
        img = img.convert("RGB")
        #lena = mpimg.imread(file)
        #img.show()
    except IOError:
        return np.zeros((size,size))
    return img

def imageToArray(im):
    im = im.convert('L')
    width,height = im.size
    data = im.getdata()
    data = np.matrix(data,dtype='float')/255.0
    new_data = np.reshape(data,(width,height))
    return new_data

def deg2num_pixel(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    xpixel = int(((lon_deg + 180.0) / 360.0 * n)*256%256 + 1/2)
    ypixel = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n  *256%256+1/2 )
    return (xtile, ytile ,xpixel,ypixel)
def real_coordinate(lat_deg,lon_deg,level):#æ ¹æ®ç»çº¬åº¦è®¡ç®å¾çåæ çå½æ°
    (xtile, ytile ,xpixel,ypixel) = deg2num_pixel(lat_deg, lon_deg, level)
    real_coordinate_x = (ytile - start_y) * size + ypixel
    real_coordinate_y = (xtile - start_x) * size + xpixel 
    return(real_coordinate_x,real_coordinate_y)

def down_a_map(time_now):

    start_x = 3168
    start_y = 1183
    level = 14
    
    
    size = 256
    x_range = 10
    y_range = 10
    tile_x =np.arange(start_x - x_range,start_x  , 1)
    tile_y =np.arange(start_y - y_range,start_y ,  1)
    myMap = np.zeros((len(tile_y)*size,len(tile_x)*size,3),dtype = 'uint8' )  
    address = 'http://its.map.baidu.com:8002/traffic/TrafficTileService?'#level=13&x=1580&y=589&time=1507687074027&v=081&smallflow=1&scaler=1
	
    for i  in range(len(tile_x)):
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

# define func let int transto two chars like 0 --> '00'
def number_to_twochars(time_num):
    twocharsstr = time_num
    twocharsstr = str(time_num)
    twocharsstr = twocharsstr.zfill(2)
    return twocharsstr
'''
#coding:UTF-8
import time

#获取当前时间
time_now = int(time.time())
#转换成localtime
time_local = time.localtime(time_now)
#转换成新的时间格式(2016-05-09 18:59:20)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

print dt

#转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = time.mktime(timeArray)

'''

#%%
#äºåéä¸æ¬¡ï¼æååäº¬å¸åºçè·¯åµå¾ï¼ä»20170101 00:00:00 å¼å§?

#ss = time_input/1000.0
#localtime = time.localtime( time.time() )
#print "æ¬å°æ¶é´ä¸?:", localtime

#hours = 5
#t = (2017, 1, 1,0, 0, 0, 1, 48, 0)
#secs = time.mktime( t )
#print "time.mktime(t) : %f" %  secs
#print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))

size = 256
address = 'http://its.map.baidu.com:8002/traffic/TrafficTileService?'#level=13&x=1580&y=589&time=1507687074027&v=081&smallflow=1&scaler=1
#time_start = 1483200000 #Sun Jan 01 00:00:00 2017

#time_start = 1472659200.0 #Thu Sep  1 00:00:00 2016
#time_now = time_start

time_now = int(time.time())
time_local = time.localtime(time_now)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

import string

dt_new = dt.replace(' ','_' )
dt_new = dt_new.replace(':','-' )

# dt_new 2018-06-25_17-22-53
print dt_new  
#trans time array
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#trans time chuo
timestamp = time.mktime(timeArray)
timestamp = timestamp *1000

#check file if exists
import os
dt_check = dt_new
dt_check_first = dt_new[:17]
second = 0
flag = 0

# check 30-60 second's data
for second in range(30,60):
    secondstr = number_to_twochars(second)
    filename = dt_check_first+secondstr+'.png'
    if os.path.exists(filename):
        flag = flag + 1

if flag >=1:
    pass
else:
    ss = down_a_map(timestamp)  
    file_name = dt_new
    plt.imsave(file_name+'.png',ss)
    print dt



# if (os.path.exists(dt_check1) or os.path.exists(dt_check2)):
#     print "file exists"
# else:
#     #下载图片 按照时间戳
#     ss = down_a_map(timestamp)  
#     #file_name = time.asctime(time.localtime(timestamp/1000))
#     #plt.imshow(ss)
#     file_name = dt_new
#     plt.imsave(file_name+'.png',ss)
#     # dt 2018-06-25 17:22:53
#     print dt
#     '''
#     for k in range(1,288 * 120):
#         time_now = time_start + 300 * k
#         time_now = time_now *1000
#         ss = down_a_map(time_now)
#         file_name = time.asctime(time.localtime(time_now/1000))
#         plt.imsave(file_name+'.jpg',ss)
#         print k
#     '''