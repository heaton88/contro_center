# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/9/14 2:02 下午
# _FileName_: daily_check.py

import requests
import json
from config_control import login,access_header,sj_list,customer_list

code_list = sj_list()[0]
name_list = sj_list()[1]
org_list = sj_list()[2]

access_token = login()[0]
refresh_token = login()[1]
userid = login()[2]
orgid = login()[3]

customer_id_list = customer_list()[0]
customer_code_list = customer_list()[1]
customer_name_list = customer_list()[2]

daily_url = 'https://yapi.golowo.com/mock/122/g3-screen-web/pingming/qualitymanagement/getWeekCheckData'
weekly_url = 'https://k8sdev.golowo.com/g3-screen-web/pingming/qualitymanagement/getWeekCheckData'
# datas1 = {'orgCode': '-5085243703379410284,0101000000', 'customerCode': '201902598,201902598'}
# dail_rep = requests.post(daily_url,headers=access_header('json'),data=json.dumps(datas1))
# print(dail_rep.json())
for i in range(0,len(orgid)):
    for j in range(0,len(customer_name_list)):
        datas = {'orgCode':  org_list[i] + ' ,' + code_list[i],'customerCode': customer_code_list[j] + ' ,' + customer_code_list[j] }
        daily_rep = requests.post(daily_url,headers=access_header('json'),data=json.dumps(datas))
        if daily_rep.status_code == 200:
            print(name_list[i],customer_name_list[j],"返回正常",daily_rep.json()['data'])
        else:
            print(name_list[i],customer_name_list[j],"返回报错",daily_rep.content)

