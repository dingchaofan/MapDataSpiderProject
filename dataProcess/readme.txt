��Щ����������ʹ������ݵ��ļ�

baidu_roadcondition_simple_2_0.py ��ʦ��д����ȡ��ͼ���ݵĽű�

check_baidu_roadcondition_simple.py ������check�ļ��Ǽ�������ļ��Ƿ���ڵĽű�����baidu_roadcondition_simple_2_0.py�м����˼���ļ����ڵĹ���

�ڷ������ϵ�cron��ʱ�� �������£�
# m h  dom mon dow   command
* * * * * cd /home/dingchaofan/map_data/ && python baidu_roadcondition_simple_2_0.py
#* * * * * sleep 20; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_0-30.py
* * * * * sleep 25; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_0-30.py
* * * * * sleep 30; cd /home/dingchaofan/map_data/ && python baidu_roadcondition_simple_2_0.py
#* * * * * sleep 50; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_30-60.py
* * * * * sleep 55; cd /home/dingchaofan/map_data/; python check_baidu_roadcondition_simple_3_30-60.py
# this is a data spyder, please don't stop it.

count_03.py��count_04.py�Ƕ��������������ݽ��д���Ľű������޳��������ݺ���һ���̶��϶Զ�ʧ�����ݽ��к�����䣬��ʾ���������ݵ�ȱʧ�����

creatFolders.py�������´���Ŀ¼��������������ʱ�Ĳ�����
