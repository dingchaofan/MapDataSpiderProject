这些是数据爬虫和处理数据的文件

baidu_roadcondition_simple_2_0.py 是师兄写的爬取地图数据的脚本

check_baidu_roadcondition_simple.py 这两个check文件是检查数据文件是否存在的脚本，在baidu_roadcondition_simple_2_0.py中加入了检查文件存在的功能

在服务器上的cron定时器 设置如下：
# m h  dom mon dow   command
* * * * * cd /home/dingchaofan/map_data/ && python baidu_roadcondition_simple_2_0.py
#* * * * * sleep 20; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_0-30.py
* * * * * sleep 25; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_0-30.py
* * * * * sleep 30; cd /home/dingchaofan/map_data/ && python baidu_roadcondition_simple_2_0.py
#* * * * * sleep 50; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_30-60.py
* * * * * sleep 55; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_30-60.py
# this is a data spyder, please don't stop it.

count_03.py和count_04.py是对下载下来的数据进行处理的脚本，会剔除冗余数据和在一定程度上对丢失的数据进行合理填充，显示出当日数据的缺失情况。

creatFolders.py根据年月创建目录，便于数据下载时的操作。
