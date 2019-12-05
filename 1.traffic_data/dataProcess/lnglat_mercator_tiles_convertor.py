# -*- coding: utf-8 -*-
import json
import urllib
import math

# 常量
x_pi = 3.14159265358979324 * 3000.0 / 180.0
pi = 3.1415926535897932384626  # π
a = 6378245.0  # 长半轴
ee = 0.00669342162296594323  # 偏心率平方

# for example:tiles start from (3158,1173) to (3167,1182), left_bottom to right_top
# 对于每个瓦片来讲，像素点从左下角开始算

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
def point2tiles_pixel(pointX,pointY,level=14):
	tileX = int(pointX * (2 ** (level - 18)) / 256)
	tileY = int(pointY * (2 ** (level - 18)) / 256)
	pixelX = int(pointX * (2 ** (level - 18)) - tileX * 256 + 0.5)
	pixelY = int(pointY * (2 ** (level - 18)) - tileY * 256 + 0.5)
	return(tileX,tileY,pixelX,pixelY)
# 瓦片（tileX， tileY）和像素坐标（pixelX, pixelY）转平面坐标（pointX, pointY）
# tile coordinates（tileX， tileY）and pixel coordinates（pixelX, pixelY）in tiles convert to plane coordinates（pointX, pointY）
def tiles_pixel2point(tileX, tileY, pixelX, pixelY, level=14):
	pointX = round(((tileX * 256 + pixelX) / (2 ** (level - 18))),1)
	pointY = round(((tileY * 256 + pixelY) / (2 ** (level - 18))),1)
	return(pointX,pointY) 


# 以下的函数暂时没有用到    
# degree of longitude 经度 latitude 纬度    
# OpenStreetMap经纬度转行列号 不准确的OpenStreetMap用的是WGS84 百度用的是BD09
# OpenStreetMap use WGS84, Baidu use BD09

def out_of_china(lng, lat):
    """
    判断是否在国内，不在国内不做偏移
    :param lng:
    :param lat:
    :return:
    """
    return not (lng > 73.66 and lng < 135.05 and lat > 3.86 and lat < 53.55)


def _transformlat(lng, lat):
    ret = -100.0 + 2.0 * lng + 3.0 * lat + 0.2 * lat * lat + \
          0.1 * lng * lat + 0.2 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lat * pi) + 40.0 *
            math.sin(lat / 3.0 * pi)) * 2.0 / 3.0
    ret += (160.0 * math.sin(lat / 12.0 * pi) + 320 *
            math.sin(lat * pi / 30.0)) * 2.0 / 3.0
    return ret


def _transformlng(lng, lat):
    ret = 300.0 + lng + 2.0 * lat + 0.1 * lng * lng + \
          0.1 * lng * lat + 0.1 * math.sqrt(math.fabs(lng))
    ret += (20.0 * math.sin(6.0 * lng * pi) + 20.0 *
            math.sin(2.0 * lng * pi)) * 2.0 / 3.0
    ret += (20.0 * math.sin(lng * pi) + 40.0 *
            math.sin(lng / 3.0 * pi)) * 2.0 / 3.0
    ret += (150.0 * math.sin(lng / 12.0 * pi) + 300.0 *
            math.sin(lng / 30.0 * pi)) * 2.0 / 3.0
    return ret

def deg2num_pixel(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg) # 返回一个角度的弧度值
    n = 2.0 ** zoom # 乘方
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    xpixel = int(((lon_deg + 180.0) / 360.0 * n)*256%256 + 1/2)
    ypixel = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n  *256%256+1/2 )
    return (xtile, ytile ,xpixel,ypixel)
def real_coordinate(lat_deg,lon_deg,level):# 真实坐标
    (xtile, ytile ,xpixel,ypixel) = deg2num_pixel(lat_deg, lon_deg, level)
    start_x = 3168
    start_y = 1183
    real_coordinate_x = (ytile - start_y) * size + ypixel
    real_coordinate_y = (xtile - start_x) * size + xpixel 
    return(real_coordinate_x,real_coordinate_y)
    
# the convert function of GCJ02 and BD09
# GCJ02的坐标和BD09的坐标转换是双向的，转换规则可以参考下面的python代码
x_pi = 3.14159265358979324 * 3000.0 / 180.0
def gcj02_to_bd09(amap_lon, amap_lat):
    """
    火星坐标系(GCJ-02)转百度坐标系(BD-09)
    谷歌、高德——>百度
    :param amap_lon:火星坐标经度
    :param amap_lat:火星坐标纬度
    :return:转换后的百度坐标形式
    """
    x = amap_lon
    y = amap_lat
    z = math.sqrt(x * x + y * y) + 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) + 0.000003 * math.cos(x * x_pi)
    bmap_lon = round((z * math.cos(theta) + 0.0065),6)
    bmap_lat = round((z * math.sin(theta) + 0.006),6)
    return (bmap_lon, bmap_lat)

def bd09_to_gcj02(bmap_lon, bmap_lat):
    """
    百度坐标系(BD-09)转火星坐标系(GCJ-02)
    百度——>谷歌、高德
    :param bmap_lon:百度坐标经度
    :param bmap_lat:百度坐标纬度
    :return:转换后的火星坐标形式
    """
    x = bmap_lon - 0.0065
    y = bmap_lat - 0.006;
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * x_pi)
    theta = math.atan2(y, x) - 0.000003 * math.cos(x * x_pi)
    amap_lon = round((z * math.cos(theta)),6)
    amap_lat = round((z * math.sin(theta)),6)
    return (amap_lon, amap_lat) 

def wgs84_to_gcj02(lng, lat):
    """
    WGS84转GCJ02(火星坐标系)
    :param lng:WGS84坐标系的经度
    :param lat:WGS84坐标系的纬度
    :return:
    """
    if out_of_china(lng, lat):  # 判断是否在国内
        return (lng, lat)
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = round((lat + dlat),6)
    mglng = round((lng + dlng),6)
    return (mglng, mglat)

def gcj02_to_wgs84(lng, lat):
    """
    GCJ02(火星坐标系)转GPS84
    :param lng:火星坐标系的经度
    :param lat:火星坐标系纬度
    :return:
    """
    if out_of_china(lng, lat):
        return (lng, lat)
    dlat = _transformlat(lng - 105.0, lat - 35.0)
    dlng = _transformlng(lng - 105.0, lat - 35.0)
    radlat = lat / 180.0 * pi
    magic = math.sin(radlat)
    magic = 1 - ee * magic * magic
    sqrtmagic = math.sqrt(magic)
    dlat = (dlat * 180.0) / ((a * (1 - ee)) / (magic * sqrtmagic) * pi)
    dlng = (dlng * 180.0) / (a / sqrtmagic * math.cos(radlat) * pi)
    mglat = round((lat + dlat),6)
    mglng = round((lng + dlng),6)
    return (round((lng * 2 - mglng),6), round((lat * 2 - mglat),6))

def bd09_to_wgs84(bd_lon, bd_lat):
    lon, lat = bd09_to_gcj02(bd_lon, bd_lat)
    return gcj02_to_wgs84(lon, lat)

def wgs84_to_bd09(lon, lat):
    lon, lat = wgs84_to_gcj02(lon, lat)
    return gcj02_to_bd09(lon, lat)