这些是数据爬虫和处理数据的文件

baidu_roadcondition_simple_2_0.py 是师兄写的爬取地图数据的脚本

check_baidu_roadcondition_simple.py 这两个check文件是检查数据文件是否存在的脚本，在baidu_roadcondition_simple_2_0.py中加入了检查文件存在的功能

在服务器上的cron定时器 设置如下：
# m h  dom mon dow   command
* * * * * cd /home/dingchaofan/map_data/; python baidu_roadcondition_simple_2_0.py
#* * * * * sleep 20; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_0-30.py
* * * * * sleep 25; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_0-30.py
* * * * * sleep 30; cd /home/dingchaofan/map_data/; python baidu_roadcondition_simple_2_0.py
#* * * * * sleep 50; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_30-60.py
* * * * * sleep 55; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_30-60.py
# this is a data spyder, please don't stop it.
* * * * * cd /home/dingchaofan/map_data_circle6/; python baidu_roadcondition_simple_2_0.py
* * * * * sleep 25; cd /home/dingchaofan/map_data_circle6/; python check_baidu_roadcondition_simple_3_0-30.py
* * * * * sleep 30; cd /home/dingchaofan/map_data_circle6/; python baidu_roadcondition_simple_2_0.py
* * * * * sleep 55; cd /home/dingchaofan/map_data_circle6/; python check_baidu_roadcondition_simple_3_30-60.py

* * * * *  cd /home/dingchaofan/mapdata_partof16/ && python check_baidu_roadcondition_simple_3_0.py
* * * * * sleep 58;cd /home/dingchaofan/mapdata_partof16/ && python check_baidu_roadcondition_simple_3_0.py

count_03.py和count_04.py是对下载下来的数据进行处理的脚本，会剔除冗余数据和在一定程度上对丢失的数据进行合理填充，显示出当日数据的缺失情况。

creatFolders.py根据年月创建目录，便于数据下载时的操作。
将服务器上的三个tempdata文件下载到本地的map_partof16的每一日的dir中，movefiles.py将tempdata中的data分别移动到不同的文件夹中。

pyfiles_server中的MoveDataToTemp.py和DeleteDataInTemp.py以在ubuntu命令行传参的方式取代以下的ubuntu的命令行指令，简化重复的操作。
python MoveDataToTemp.py 2019 03 09取代
find "/home/dingchaofan/map_data/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata/"
find "/home/dingchaofan/map_data_circle6/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata1/"
find "/home/dingchaofan/mapdata_partof16/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata2/"
python DeleteDataInTemp.py 2019 03 09取代在tempdata tempdata1 tempdata2中执行
find . -type f -name "*2019-03-09*" -delete
 



