# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:17:28 2017

@author: zhangqi
"""

"""
rewrite this file, change it to python3 Sat 
	Oct 27 20:08:19 2018

add functions of convert in BD09 longitude and latitude degree, 
plane coordinates of Mercator projection, tile coordinates（tileX,tileY）
and pixel coordinates（pixelX, pixelY）in tiles
	Fri Nov 09 15:44:37 2018

@author: dingchaofan
"""

try:#python2
    import urllib2
    import cStringIO
except ImportError:#python3
    import urllib.request
    import io

import matplotlib.pyplot as plt
import time
import numpy as np
import math
import sys
from PIL import Image

# show tile pictures 256*256
def showBmap(my_url):
    try:#python2
        file = cStringIO.StringIO(urllib2.urlopen(my_url).read())
    except NameError:#python3
        file = io.BytesIO(urllib.request.urlopen(my_url).read())
    try:
        img = Image.open(file)
        img = img.convert("RGB")
        #lena = mpimg.imread(file)
        #img.show()
    except IOError:
        print('fail to convert')
        return np.zeros((size,size))
    return img

# miaomiaomiao？ unused function
# def imageToArray(im):
#     im = im.convert('L')
#     width,height = im.size
#     data = im.getdata()
#     data = np.matrix(data,dtype='float')/255.0
#     new_data = np.reshape(data,(width,height))
#     return new_data

# degree of longitude 经度 latitude 纬度    
# OpenStreetMap经纬度转行列号 不准确的 OpenStreetMap用的是WGS84 百度用的是BD09
# OpenStreetMap use WGS84, Baidu use BD09
def deg2num_pixel(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg) # 返回一个角度的弧度值
    n = 2.0 ** zoom # 乘方
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    xpixel = int(((lon_deg + 180.0) / 360.0 * n)*256%256 + 1/2)
    ypixel = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n  *256%256+1/2 )
    return (xtile, ytile ,xpixel,ypixel)
def real_coordinate(lat_deg,lon_deg,level):#æ ¹æ®ç»çº¬åº¦è®¡ç®å¾çåæ çå½æ°
    (xtile, ytile ,xpixel,ypixel) = deg2num_pixel(lat_deg, lon_deg, level)
    start_x = 3168
    start_y = 1183
    real_coordinate_x = (ytile - start_y) * size + ypixel
    real_coordinate_y = (xtile - start_x) * size + xpixel 
    return(real_coordinate_x,real_coordinate_y)

# 加密解密算法函数和参数
# encryption and decryption function and parameters
xu = 6370996.81
Sp = [1.289059486E7, 8362377.87, 5591021, 3481989.83, 1678043.12, 0]
Hj = [75, 60, 45, 30, 15, 0]
Au = [[1.410526172116255E-8, 8.98305509648872E-6, -1.9939833816331, 200.9824383106796, -187.2403703815547, 91.6087516669843, -23.38765649603339, 2.57121317296198, -0.03801003308653, 1.73379812E7], [ - 7.435856389565537E-9, 8.983055097726239E-6, -0.78625201886289, 96.32687599759846, -1.85204757529826, -59.36935905485877, 47.40033549296737, -16.50741931063887, 2.28786674699375, 1.026014486E7], [ - 3.030883460898826E-8, 8.98305509983578E-6, 0.30071316287616, 59.74293618442277, 7.357984074871, -25.38371002664745, 13.45380521110908, -3.29883767235584, 0.32710905363475, 6856817.37], [ - 1.981981304930552E-8, 8.983055099779535E-6, 0.03278182852591, 40.31678527705744, 0.65659298677277, -4.44255534477492, 0.85341911805263, 0.12923347998204, -0.04625736007561, 4482777.06], [3.09191371068437E-9, 8.983055096812155E-6, 6.995724062E-5, 23.10934304144901, -2.3663490511E-4, -0.6321817810242, -0.00663494467273, 0.03430082397953, -0.00466043876332, 2555164.4], [2.890871144776878E-9, 8.983055095805407E-6, -3.068298E-8, 7.47137025468032, -3.53937994E-6, -0.02145144861037, -1.234426596E-5, 1.0322952773E-4, -3.23890364E-6, 826088.5]]
Qp = [[- 0.0015702102444, 111320.7020616939, 1704480524535203, -10338987376042340, 26112667856603880, -35149669176653700, 26595700718403920, -10725012454188240, 1800819912950474, 82.5], [8.277824516172526E-4, 111320.7020463578, 6.477955746671607E8, -4.082003173641316E9, 1.077490566351142E10, -1.517187553151559E10, 1.205306533862167E10, -5.124939663577472E9, 9.133119359512032E8, 67.5], [0.00337398766765, 111320.7020202162, 4481351.045890365, -2.339375119931662E7, 7.968221547186455E7, -1.159649932797253E8, 9.723671115602145E7, -4.366194633752821E7, 8477230.501135234, 52.5], [0.00220636496208, 111320.7020209128, 51751.86112841131, 3796837.749470245, 992013.7397791013, -1221952.21711287, 1340652.697009075, -620943.6990984312, 144416.9293806241, 37.5], [ - 3.441963504368392E-4, 111320.7020576856, 278.2353980772752, 2485758.690035394, 6070.750963243378, 54821.18345352118, 9540.606633304236, -2710.55326746645, 1405.483844121726, 22.5], [ - 3.218135878613132E-4, 111320.7020701615, 0.00369383431289, 823725.6402795718, 0.46104986909093, 2351.343141331292, 1.58060784298199, 8.77738589078284, 0.37238884252424, 7.45]]

def Convertor(x,y,arr):
    pass
    x_temp = arr[0] + arr[1]*abs(x)
    y_temp = abs(y)/arr[9]
    y_temp1 = arr[2] + arr[3]*y_temp + arr[4]*y_temp*y_temp + arr[5]*y_temp*y_temp*y_temp + arr[6]*y_temp*y_temp*y_temp*y_temp + arr[7]*y_temp*y_temp*y_temp*y_temp*y_temp + arr[8]*y_temp*y_temp*y_temp*y_temp*y_temp*y_temp
    # c = c * (0 > a.lng ? -1 : 1) ternary operator of python like that:
    # python中的三元运算符写法：
    x_Converted = x_temp * (-1 if(0 > x) else 1)
    y_Converted = y_temp1 * (-1 if(0 > y) else 1)
    return[x_Converted,y_Converted]

# BD09经纬度和墨卡托投影的平面坐标的相互转换函数
# the convert function of longitude and latitude degree of BD09 and  plane coordinates of Mercator projection 
def BD092mercotor(lng_BD09,lat_BD09):
    arr = []
    lat_abs = abs(lat_BD09)
    for i in range(len(Hj)):
        if (lat_abs >= Hj[i]):
            arr = Qp[i]
            break
    res = Convertor(lng_BD09,lat_BD09,arr)
    pointX = round(res[0],1)
    pointY = round(res[1],1)
    return (pointX,pointY)
def mercator2BD09(pointX,pointY):
    arr = []
    pointYabs = abs(pointY)
    for i in range(len(Sp)):
        if (pointYabs >= Sp[i]):
            arr = Au[i]
            break
    res = Convertor(pointX,pointY,arr)
    lng_BD09 = round(res[0],6)
    lat_BD09 = round(res[1],6)
    return (lng_BD09,lat_BD09)

# 平面坐标（pointX, pointY）转瓦片坐标（tileX， tileY）和瓦片中的像素坐标（pixelX, pixelY）
# plane coordinates（pointX, pointY）convert to tile coordinates（tileX， tileY）and pixel coordinates（pixelX, pixelY）in tiles
def point2tiles_pixel(pointX,pointY,level):
	tileX = int(pointX * (2 ** (level - 18)) / 256)
	tileY = int(pointY * (2 ** (level - 18)) / 256)
	pixelX = int(pointX * (2 ** (level - 18)) - tileX * 256 + 0.5)
	pixelY = int(pointY * (2 ** (level - 18)) - tileY * 256 + 0.5)
	return(tileX,tileY,pixelX,pixelY)
# 瓦片（tileX， tileY）和像素坐标（pixelX, pixelY）转平面坐标（pointX, pointY）
# tile coordinates（tileX， tileY）and pixel coordinates（pixelX, pixelY）in tiles convert to plane coordinates（pointX, pointY）
def tiles_pixel2point(tileX, tileY, pixelX, pixelY, level):
	pointX = round(((tileX * 256 + pixelX) / (2 ** (level - 18))),1)
	pointY = round(((tileY * 256 + pixelY) / (2 ** (level - 18))),1)
	return(pointX,pointY) 
    

def down_a_map(time_now):

    start_x = 3168
    start_y = 1183
    level = 14
      
    size = 256
    x_range = 10
    y_range = 10
    # tile_x,tile_y is (10,)
    tile_x =np.arange(start_x - x_range,start_x , 1)
    tile_y =np.arange(start_y - y_range,start_y , 1)
    # creat a 3 axis array. The size of myMap is (2560,2560,3), type is uint8
    myMap = np.zeros((len(tile_y)*size,len(tile_x)*size,3),dtype = 'uint8' )  
    address = 'http://its.map.baidu.com:8002/traffic/TrafficTileService?' # level=13&x=1580&y=589&time=1507687074027&v=081&smallflow=1&scaler=1
	
	# tiles start from (3158,1173) to (3167,1182), left_bottom to right_top
	# i,j is in 1~10
    for i  in range(len(tile_x)):
        # print(i)
        for j in range(len(tile_y)):
            print(i,j)
            #url_ij = address+('x=%d&y=%d&z=%d')%(tile_x[i],tile_y[j],level)
            url_ij = address+('level=%d&x=%d&y=%d&time=%d')%(level,tile_x[i],tile_y[j],time_now)
            # print(url_ij)
            temp = showBmap(url_ij)
            # if url_ij can be convert to RGB, temp.size = (256,256)
            # print(temp.size)
            # If this tile is empty, there is no way in picture. 
            # temp = np.zeros((256,256)). temp.size=65536. Otherwise, temp.size=(256,256)
            if temp.size == 65536:
                print('There is no way in this tile')
                temp_3 =np.zeros((256,256,3))
                temp_3[:,:,0] = temp
                temp_3[:,:,1] = temp
                temp_3[:,:,2] = temp
                temp = temp_3
            # 10*10 tiles convert to a png
            myMap[ (y_range-j-1)*size:(y_range-j)*size ,i*size:(i+1)*size   ,: ] = np.array(temp)
            # position = real_coordinate(tile_x[i],tile_y[j],level)
            # print(position)
    return myMap


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

size = 256
#address = 'http://its.map.baidu.com:8002/traffic/TrafficTileService?'#level=13&x=1580&y=589&time=1507687074027&v=081&smallflow=1&scaler=1
#time_start = 1483200000 #Sun Jan 01 00:00:00 2017

#time_start = 1472659200.0 #Thu Sep  1 00:00:00 2016
#time_now = time_start

time_now = int(time.time())
time_local = time.localtime(time_now)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)

dt_new = dt.replace(' ','_' )
dt_new = dt_new.replace(':','-' )
print(dt_new)
# convert to time array
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
# convert to timestamp
timestamp = time.mktime(timeArray)
timestamp = timestamp *1000
ss = down_a_map(timestamp)
#file_name = time.asctime(time.localtime(timestamp/1000))
#plt.imshow(ss)
file_name = dt_new
plt.imsave(file_name+'.png',ss)
print(dt)


'''
for k in range(1,288 * 120):
    time_now = time_start + 300 * k
    time_now = time_now *1000
    ss = down_a_map(time_now)
    file_name = time.asctime(time.localtime(time_now/1000))
    plt.imsave(file_name+'.jpg',ss)
    print k
'''