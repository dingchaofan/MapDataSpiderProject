# MapDataSpiderProject

交通数据爬虫项目说明文档

## 项目结构说明

```shell
MapDataSpiderProject
├─README.md                                                 # 项目说明文档
├─dataVisualization                                         # 最初的数据可视化项目，现已废弃
├─2.yang_traffic_data                                       # 北京市交通委数据爬虫项目
|       ├─creatFolders.py                                   # 创建当月每天目录
|       ├─movefiles.py                                      # 将tempdata目录中的数据移动到每天的目录下
|       ├─traffic_data.py                                   # 北京交通委数据爬虫
|       └ 格式.json                                          # 数据格式样例
├─1.traffic_data                                            # 百度地图数据爬虫
|       ├─dataProcess
|       |      ├─lnglat_mercator_tiles_convertor.py         # 经纬度坐标系转换，最新功能看traffic-vis的后端项目中此程序文件
|       |      ├─readme.txt
|       |      ├─数据说明.docx
|       |      ├─pyfiles_server                             # 服务器中部署运行的python程序
|       |      |       ├─DeleteDataInTemp.py                # 删除tempdata目录下的数据文件
|       |      |       ├─MoveDataToTemp.py                  # 将某日的数据文件移动到tampdata中
|       |      |       ├─old_map_data
|       |      |       ├─map_data_level16                   # 16级地图数据爬虫
|       |      |       |        └baidu_roadcondition_py23.py
|       |      |       ├─map_data_level14                   # 14级地图数据爬虫
|       |      |       |        └baidu_roadcondition_py23.py
|       |      ├─data_count
|       |      |     ├─map_data_level16                     # 16级数据本地存储目录
|       |      |     |        ├─countAll.py                 # 统计当月每日的数据情况
|       |      |     |        ├─count_05.py                 # 统计当日数据情况
|       |      |     |        ├─creatFolders.py             # 创建每日目录
|       |      |     |        ├─movefiles.py                # 移动数据到每日
|       |      |     |        └数据情况level16.xlsx          # 16级数据情况统计表
|       |      |     ├─map_data_level14                     # 14级数据本地存储目录
|       |      |     |        ├─countAll.py                 # 统计当月每日的数据情况
|       |      |     |        ├─count_05.py                 # 统计当日数据情况
|       |      |     |        ├─creatFolders.py             # 创建每日目录
|       |      |     |        └数据情况level14.xlsx          # 16级数据情况统计表
```

### dataVisualization 项目

此项目已废弃，采用扩展性更好的前后端分离项目替代

前端 https://github.com/dingchaofan/traffic-vis-fe
后端 https://github.com/dingchaofan/flask-learn

`dataVisualization`目录下
map road data visualization with echarts tool
交通数据可视化 用echarts工具将道路拥堵情况的数据以热力图的形式展现在web页面中

dataVisualization文件夹是数据的转换和可视化，将png数据批量转换成json格式数据，将json数据可视化在web页面中
<!-- 项目文件夹在 E:\CAS\CodeFile\forgit\MapDataVisualizationProject
在git bash中 cd E:\CAS\CodeFile\forgit\MapDataVisualizationProject 进入目录 -->


## 服务器中部署

采用linux自带的定时器crontab，使用方法可参考：[Linux crontab命令：循环执行定时任务（详解版）](http://c.biancheng.net/view/1092.html)

* 需自行学习vi、vim的使用方法

* 常用命令

    ```shell
    crontab -l  # 查看crontab脚本
    crontab -e  # 编辑crontab脚本
    ```

* 在crontab的脚本中定时执行`baidu_roadcondition_py23.py`python程序，进行爬虫下载任务，命令是带参数的

    ```shell
    python baidu_roadcondition_py23.py 14 0  # 下载14级图片
    python baidu_roadcondition_py23.py 16 0  # 下载16级图片
    ```

* 运行环境python 3.7，所需python依赖库可自行安装

* **注意事项：**
  * **http请求并发数不要过高，会有被百度封禁IP的风险**
  * 建议每台服务器每分钟的程序并发数量不要超过4。
  * 多线程会加快每张图片的下载速度，但是提高线程数也会增加IP封禁的风险。
  * 有需求尽量用增加服务器的方式实现。

### 数据采集实际部署情况说明

1. 154服务器：
   1. 采集百度道路拥堵图片数据
   2. 14级数据1分钟1次，每分钟的第0秒进行采集
   3. 16级数据2分钟1次，奇数分钟第0秒进行采集
2. 194服务器：
   1. 采集百度道路拥堵图片数据
   2. 14级数据1分钟1次，每分钟的第30秒进行采集
   3. 16级数据2分钟1次，偶数分钟第0秒进行采集
3. 195服务器：
   1. 采集北京市交通委json数据
   2. 每分钟一次
   3. 不能采集百度道路拥堵图片数据了，IP已被百度封禁

### 数据采集的人工操作流程

```shell
python MoveDataToTemp.py 2021 01 18     # 将map_data_level14、map_data_level16目录中当天的数据文件移动到tempdata14、tempdata16中
# 手动下载数据，推荐使用软件WinScp，下载速度快
python DeleteDataInTemp.py 2021 01 18    # 删除tempdata14、tempdata16中数据
```
