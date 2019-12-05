# coding: utf-8

import requests
import json
import time

# while(0):
#     last_min = time.strftime("%M", time.localtime())
#     while(1):
#         # get data per minute
#         if last_min == time.strftime("%M", time.localtime()):
#             time.sleep(20)
#         else:
#             break

#     url = 'http://eye.bjjtw.gov.cn/Web-T_bjjt_new/query.do?serviceType=jam&acode=110000&type=1&cls=0&rcd=300'
#     headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Host': 'eye.bjjtw.gov.cn', 'Upgrade-Insecure-Requests': '1', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0', 'user-agent': 'my-app/0.0.1'}
#     r = requests.get(url, headers=headers)
#     # some place's 'lonlat' is '[,]', replace to '[999,999]'
#     r_str = r.text.replace('[,]', '[999,999]')
#     r_dic = json.loads(r_str)

#     localtime = time.strftime("%Y-%m-%d %H:%M", time.localtime()).replace(':','_')
#     with open(localtime + '.json', 'w') as f:
#         json.dump(r_dic, f, ensure_ascii=False)
#     print(localtime)


url = 'http://service.jtw.beijing.gov.cn/sslk/Web-T_bjjt_new/query.do?serviceType=jam&acode=110000&type=1&cls=0&rcd=300'
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate','Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Host': 'eye.bjjtw.gov.cn', 'Upgrade-Insecure-Requests': '1', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0', 'user-agent': 'my-app/0.0.1'}
# r = requests.get(url, headers=headers)
r = requests.get(url)
# some place's 'lonlat' is '[,]', replace to '[999,999]'
r_str = r.text.replace('[,]', '[999,999]')
r_dic = json.loads(r_str)

localtime = time.strftime("%Y-%m-%d %H:%M", time.localtime()).replace(':','_')
with open(localtime + '.json', 'w') as f:
    json.dump(r_dic, f, ensure_ascii=False)
print(localtime)