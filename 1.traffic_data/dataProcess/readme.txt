数据爬虫和处理数据的文件
2019.12.05更新

baidu_roadcondition_py23.py 是爬取地图数据的脚本，推荐使用python3，根据传入参数确定地图等级

# 已废弃
# check_baidu_roadcondition_simple.py 这两个check文件是检查数据文件是否存在的脚本，在baidu_roadcondition_simple_2_0.py中加入了检查文件存在的功能

在服务器上的cron定时器 crontab -e 编辑 crontab -l 查看
设置如下：
# m h  dom mon dow   command
MAILTO=""
# for level 14
* * * * * cd /home/dingchaofan/map_data_level14/; /home/dingchaofan/anaconda3/bin/python baidu_roadcondition_py23.py 14 0;
* * * * * sleep 30; cd /home/dingchaofan/map_data_level14/; /home/dingchaofan/anaconda3/bin/python baidu_roadcondition_py23.py 14 0;

MAILTO=""
# map_data clawer for level16
* * * * * cd /home/dingchaofan/map_data_level16; /home/dingchaofan/.conda/envs/python3_ding/bin/python baidu_roadcondition_py23.py 16 0;

count_05.py对下载下来的数据进行处理，会剔除冗余数据和在一定程度上对丢失的数据进行合理填充，显示出当日数据的缺失情况，数据情况写入execl
countAll.py执行所有目录下的count_05.py
creatFolders.py根据年月创建目录，便于数据下载时的操作。

# 已废弃
# 将服务器上的三个tempdata文件下载到本地的map_partof16的每一日的dir中，movefiles.py将tempdata中的data分别移动到不同的文件夹中。

pyfiles_server中的MoveDataToTemp.py和DeleteDataInTemp.py以在ubuntu命令行传参的方式取代以下的ubuntu的命令行指令，简化重复的操作。
python MoveDataToTemp.py 2019 03 09取代以下命令
find "/home/dingchaofan/map_data/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata/"
find "/home/dingchaofan/map_data_circle6/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata1/"
find "/home/dingchaofan/mapdata_partof16/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata2/"
python DeleteDataInTemp.py 2019 03 09取代在tempdata tempdata1 tempdata2目录中执行
find . -type f -name "*2019-03-09*" -delete


 



