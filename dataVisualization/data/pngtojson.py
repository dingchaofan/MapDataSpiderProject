# coding=utf-8
from PIL import Image
import numpy as np
import json,os
import shutil
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

testpic = "test.png"

def loadImage(filename,width0=640,hight0=640):
    
    # 读取图片
    im = Image.open(filename)
    hight, width = im.size
    # print (width,hight) # 图片大小
    
    # 压缩图片
    im_resize = im.resize((width0,hight0))
    hight, width = im_resize.size
    # print (width,hight) # 图片大小
    
    pixelColorArray = np.zeros((hight,width))
    for i in range(width):
        for j in range(hight):
            pixelRGBA = im_resize.getpixel((i,j))
            # 绿色像素 通畅 
            if pixelRGBA == (79, 209, 125, 255):
                pixelColorArray[j][i] = 5
            # 红色像素    
            if pixelRGBA == (232, 12, 12, 255):
                pixelColorArray[j][i] = 255
                # print('red',i,j)
            # 黄色像素
            if pixelRGBA == (255, 209, 69, 255):
                pixelColorArray[j][i] = 100
            # print('yellow',i,j)
            # 其他颜色的 舍去吧
            else:
                pass

    # 转换并显示灰度图片 L  貌似并不需要这部分功能啊
#    new_im = Image.fromarray(pixelColorArray)
#    new_im = new_im.convert('L')
#    # 显示灰度图片 L
#    new_im.show()
#    new_im.save('Lpic'+'.png')

    # 返回一个RGBA的list？ 不是list而是numpy.ndarray
    return pixelColorArray,filename

def resizeImage(filename,width0=640,hight0=640):
    # 读取图片
    im = Image.open(filename)
    hight, width = im.size
    # print (width,hight) # 图片大小

    im_resize = im.resize((width0,hight0))
    im_resize.save('resizedImage.png')



# dataNum = loadImage("2018-06-24_18-20-01.png").tolist()
# dataNum = loadImage("resizedImage.png").tolist()
# list矩阵
# print(type(dataNum))

def createJsonData(dataNum,filename):
    # 地图的坐标点
    hight = len(dataNum[0])
    width = len(dataNum[1])
    dataPosition = np.zeros((width,hight,2))
    k = 2560/width
    center = [116.403968,39.915122],
    left_top = [116.198442,40.050129]  #左上角坐标
    dataPosition[0][0]= left_top  
    step1 = 0.0001433*k #步长1 控制横坐标
    step2 = 0.0001105*k #步长2 控制纵坐标
    # 生成dataPosition
    for i in range(width):
        n1 = left_top[0] + i * step1
        for j in range(hight):
            dataPosition[j][i][0] = n1
            dataPosition[j][i][1] = left_top[1] - j * step2

    dataList = dataPosition.tolist()
    # list类型

    jsonData = []
    # jsonData是list
    dataPositionOne = []
    for i in range(width):
        for j in range(hight):
            dataPositionOne = dataList[i][j]
            dataPositionValue = dataNum[i][j]
            if(dataPositionValue > 10):
                DataOne = {"coord":dataPositionOne,"elevation":dataPositionValue} 
                jsonData.append(DataOne)
    # 将数据写入json文件中
    filename0 = filename.split('.')[0]
    jsonName = filename0 + ".json"
    f = open(jsonName,'w')
    f.write('[')
    f.write(json.dumps(jsonData))
    f.write(']')
    f.close()
    return jsonName

# define func let int transto two chars like 0 --> '00'
def number_to_twochars(time_num):
    twocharsstr = time_num
    twocharsstr = str(time_num)
    twocharsstr = twocharsstr.zfill(2)
    return twocharsstr

# 选择文件夹 批量转换png到json
def batchConversion():
    pass
    rootDirPath = os.getcwd()
    filesInRoot = os.listdir()
    for file in filesInRoot:
        print(filesInRoot.index(file),file)    
    while 1:
        chooseNum = input("please choose a dir to translate:")
        if((os.path.isdir(filesInRoot[int(chooseNum)]) == False) or len(filesInRoot[int(chooseNum)]) > 11):
            print("input error")      
        else:
            chooseNum = int(chooseNum)
            jsonFile = filesInRoot[chooseNum]+"-json"
            if(os.path.exists(jsonFile) == False):
                os.mkdir(jsonFile)    
            os.chdir(filesInRoot[chooseNum])
            pngDataPath = os.getcwd()
            # 用\转义\
            jsonDataPath = rootDirPath + '\\'  + filesInRoot[chooseNum] + '-json'
            break
    pngFilesInDir = os.listdir()
    jsonNameList = filesInRoot[chooseNum] + "-jsonNameList.txt"
    jsonList = open(jsonNameList,'w')
    for filename in pngFilesInDir:
        targetJsonName = jsonDataPath + '\\' + filename.split('.')[0] + ".json"
        if(os.path.exists(targetJsonName) == True):
            print(targetJsonName,"is exists")
        else:                
            dataNum,filename = loadImage(filename)
            jsonFile = createJsonData(dataNum,filename) 
            shutil.move(jsonFile,jsonDataPath)
            print(jsonFile,"Conversion completed")
        jsonList.write(jsonFile + ',')
    jsonList.close()
    shutil.move(jsonNameList,rootDirPath)


# def mainfunction():
#     resizeImage(testpic)
#     dataNum = loadImage(resizedImage)
#     createJsonData(dataNum)

# mainfunction()