# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/9/14 3:53 下午
# _FileName_: flycheck.py

#飞行检查接口全量数据测试
import requests
import json
from config_control import access_header,orgid,org_list,code_list,name_list

#日检接口
daily_url = 'https://k8stest.golowo.com/g3-screen-web/pingming/qualitymanagement/getDayCheckData'
#周检接口
weekly_url = 'https://k8stest.golowo.com/g3-screen-web/pingming/safemanagement/getDayCheckData'
for i in range(0,len(orgid)):
    #所有分公司，日检检查数量总和
    datas = {'orgCode':org_list[i] + ',' + code_list[i],'customerCode': ""}
    daily_rep = requests.post(weekly_url,headers=access_header('json'),data=json.dumps(datas))
    if daily_rep.status_code == 200:
        print(name_list[i],"返回正常",daily_rep.json())
    else:
        print(name_list[i],"返回报错",daily_rep.content)