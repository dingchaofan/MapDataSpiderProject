��������ʹ������ݵ��ļ�
2019.12.05����

baidu_roadcondition_py23.py ����ȡ��ͼ���ݵĽű����Ƽ�ʹ��python3�����ݴ������ȷ����ͼ�ȼ�

# �ѷ���
# check_baidu_roadcondition_simple.py ������check�ļ��Ǽ�������ļ��Ƿ���ڵĽű�����baidu_roadcondition_simple_2_0.py�м����˼���ļ����ڵĹ���

�ڷ������ϵ�cron��ʱ�� crontab -e �༭ crontab -l �鿴
�������£�
# m h  dom mon dow   command
MAILTO=""
# for level 14
* * * * * cd /home/dingchaofan/map_data_level14/; /home/dingchaofan/anaconda3/bin/python baidu_roadcondition_py23.py 14 0;
* * * * * sleep 30; cd /home/dingchaofan/map_data_level14/; /home/dingchaofan/anaconda3/bin/python baidu_roadcondition_py23.py 14 0;

MAILTO=""
# map_data clawer for level16
* * * * * cd /home/dingchaofan/map_data_level16; /home/dingchaofan/.conda/envs/python3_ding/bin/python baidu_roadcondition_py23.py 16 0;

count_05.py���������������ݽ��д������޳��������ݺ���һ���̶��϶Զ�ʧ�����ݽ��к�����䣬��ʾ���������ݵ�ȱʧ������������д��execl
countAll.pyִ������Ŀ¼�µ�count_05.py
creatFolders.py�������´���Ŀ¼��������������ʱ�Ĳ�����

# �ѷ���
# ���������ϵ�����tempdata�ļ����ص����ص�map_partof16��ÿһ�յ�dir�У�movefiles.py��tempdata�е�data�ֱ��ƶ�����ͬ���ļ����С�

pyfiles_server�е�MoveDataToTemp.py��DeleteDataInTemp.py����ubuntu�����д��εķ�ʽȡ�����µ�ubuntu��������ָ����ظ��Ĳ�����
python MoveDataToTemp.py 2019 03 09ȡ����������
find "/home/dingchaofan/map_data/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata/"
find "/home/dingchaofan/map_data_circle6/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata1/"
find "/home/dingchaofan/mapdata_partof16/" -name "*2019-03-09*" |xargs -i mv {} "/home/dingchaofan/tempdata2/"
python DeleteDataInTemp.py 2019 03 09ȡ����tempdata tempdata1 tempdata2Ŀ¼��ִ��
find . -type f -name "*2019-03-09*" -delete


 



