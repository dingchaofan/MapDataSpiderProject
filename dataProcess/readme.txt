��Щ����������ʹ������ݵ��ļ�

baidu_roadcondition_simple_2_0.py ��ʦ��д����ȡ��ͼ���ݵĽű�

check_baidu_roadcondition_simple.py ������check�ļ��Ǽ�������ļ��Ƿ���ڵĽű�����baidu_roadcondition_simple_2_0.py�м����˼���ļ����ڵĹ���

�ڷ������ϵ�cron��ʱ�� �������£�
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

count_03.py��count_04.py�Ƕ��������������ݽ��д���Ľű������޳��������ݺ���һ���̶��϶Զ�ʧ�����ݽ��к�����䣬��ʾ���������ݵ�ȱʧ�����

creatFolders.py�������´���Ŀ¼��������������ʱ�Ĳ�����
���������ϵ�����tempdata�ļ����ص����ص�map_partof16��ÿһ�յ�dir�У�movefiles.py��tempdata�е�data�ֱ��ƶ�����ͬ���ļ����С�

pyfiles_server�е�MoveDataToTemp.py��DeleteDataInTemp.py����ubuntu�����д��εķ�ʽȡ�����µ�ubuntu��������ָ����ظ��Ĳ�����
python MoveDataToTemp.py 2019 03 09ȡ��
find "/home/dingchaofan/map_data/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata/"
find "/home/dingchaofan/map_data_circle6/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata1/"
find "/home/dingchaofan/mapdata_partof16/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata2/"
python DeleteDataInTemp.py 2019 03 09ȡ����tempdata tempdata1 tempdata2��ִ��
find . -type f -name "*2019-03-09*" -delete
 



