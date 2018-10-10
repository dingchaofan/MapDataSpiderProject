import os
import string
import sys

# 获取脚本名的两个方法 输出脚本名
# print(__file__)  
# print(sys.argv[0])

# 获取执行脚本的目录 输出绝对路径
# print(sys.path[0])   
# print(os.getcwd())

# split方法 输出文件名
# print(os.path.split(os.getcwd()))
# print(os.path.split(__file__)[-1])
# print(os.path.split(__file__)[-1].split('.')[0])
# 输出文件的真实路径和所在文件夹的路径
# print(os.path.realpath(__file__))
# print(os.path.dirname(os.path.realpath(__file__)))

# 获取文件夹名
dirname =  os.path.split(os.getcwd())[-1]

# 定义一个数字转两位字符串的函数 0 --> '00'
def number_to_twochars(time_num):
	twocharsstr = time_num
	twocharsstr = str(time_num)
	twocharsstr = twocharsstr.zfill(2)
	return twocharsstr


def checkdata():

	# 丢失的数据
	lostdata = []
	# 冗余的数据的
	redundantdata = []

	for hour in range(24):
		for minute in range(60):
			flag0 = 0
			flag1 = 0
			hourstr = number_to_twochars(hour)
			minutestr = number_to_twochars(minute)
			for second in range(30):
				secondstr = number_to_twochars(second)
				filename = dirname+'_'+hourstr+'-'+minutestr+'-'+secondstr+'.png'
				if os.path.isfile(filename):
					flag0 = flag0 + 1
					if flag0 >= 2:
						redundantdata.append(filename)
			for second in range(30,60):
				secondstr =number_to_twochars(second)
				filename = dirname+'_'+hourstr+'-'+minutestr+'-'+secondstr+'.png'
				if os.path.isfile(filename):
					flag1 = flag1 + 1
					if flag1 >= 2:
						redundantdata.append(filename)
			thisminutestr = dirname+'_'+hourstr+'-'+minutestr
			if flag0 >= 1:
				pass
			else:
				lostdata.append(thisminutestr + '-before.png')
			if flag1 >= 1:
				pass
			else:
				lostdata.append(thisminutestr + '-after.png')
	return lostdata, redundantdata

def reshapedata():
	pass

lostdata, redundantdata = checkdata()

# 输出丢失数据
for i in range(len(lostdata)):
	print(lostdata[i],' NO.',i)
print('the num of lostdata :',len(lostdata))
# 输出冗余数据
for i in range(len(redundantdata)):
	print(redundantdata[i],' NO.',i)
print('the num of redundantdata :',len(redundantdata))

listYes = ['y','yse','Y']
lostName = ""
# 判断是否删除冗余数据
if len(redundantdata) > 0:
	delete_instruction = input('do you want to delete redundantdata? key y/n:')
	if (delete_instruction in listYes):
		print('delete redundantdata')
		for i in range(len(redundantdata)):
			if os.path.isfile(redundantdata[i]):
				os.remove(redundantdata[i])
				# redundantdata.pop(i)
	else:
		print('save redundantdata for a while')

if len(lostdata) > 0:
	output_lostdataname = input('do you want to print lost data name? key y/n:')
	if (output_lostdataname in listYes):
		print("lostdata num is:",len(lostdata))
		for i in range(len(lostdata)):
			name = lostdata[i].split('_')[1]
			name = name.split('.')[0]
			if(len(lostName) <= 1):
				lostName = name
			else:
				lostName = lostName +'、'+ name
		print(lostName)

input('press any key to exit')