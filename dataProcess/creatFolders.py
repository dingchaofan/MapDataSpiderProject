import os
import shutil

folderNameList = []
src = "count_04.py"  #要复制的脚本名

# define func let int transto two chars like 0 --> '00'
def number_to_twochars(time_num):
    twocharsstr = time_num
    twocharsstr = str(time_num)
    twocharsstr = twocharsstr.zfill(2)
    return twocharsstr

def monthCheck(year,month):
	# a = eval(input('请输入月份：'))	 
	# while not(isinstance(a, int) and 0<a<13):
	#     a = eval(input('请输入正确的月份：'))	 
	dayue = [1,3,5,7,8,10,12]
	xiaoyue = [4,6,9,11]
	print(type(year))
	print(type(month))
	if (month in dayue):
	    print(month,'月有31天')
	    daynum = 31
	elif (month in xiaoyue):
	    print(month,'月有30天')
	    daynum = 30
	else:
	    # n=eval(input('请输入月所在年：'))
	    if  year%400==0 or (year%4==0 and year%100!=0):
	        print(year,'年为闰年',month,'月有29天')
	        daynum = 29
	    else:
	        print(year,'年为平年',month,'月有28天')
	        daynum = 28

	return daynum

def creatFloders():
	rootDirPath = os.getcwd()
	k = os.path.split(rootDirPath)
	dirName = k[1]
	year = dirName.split('-')[0]
	month = dirName.split('-')[1]
	print(dirName,year,month)

	# zfill的反向操作
	month = month.lstrip('0')
	
	year = int(year)
	month = int(month)

	daynum = monthCheck(year,month)
	print(daynum)
	for x in range(1,daynum + 1):
	    daystr = number_to_twochars(x)
	    folderName = dirName + '-' +daystr
	    if(os.path.exists(folderName) == False):
	        os.mkdir(folderName)
	        print(folderName,"is created")
	        # folderNameList.append(folderName) #不需要文件名list了
	        shutil.copy(src,folderName) #dst_dir表示目的目录
	    else:
	        print(folderName," is exists. error!!!")
            

creatFloders()
# print(folderNameList)
input('press any key to exit')