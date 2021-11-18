# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/9/14 2:02 下午
# _FileName_: daily_check.py

import requests
import json
from config_control import access_header,customer_list,code_list,name_list,org_list,orgid

#日检接口全量数据测试
customer_id_list = customer_list()[0]
customer_code_list = customer_list()[1]
customer_name_list = customer_list()[2]

daily_url = 'https://k8stest.golowo.com/g3-screen-web/pingming/qualitymanagement/getDayCheckData'
weekly_url = 'https://k8stest.golowo.com/g3-screen-web/pingming/qualitymanagement/getWeekCheckData'

for i in range(0,len(orgid)):
    for j in range(0,len(customer_name_list)):
        datas = {'orgCode':  org_list[i] + ' ,' + code_list[i],'customerCode': customer_code_list[j] + ' ,' + customer_code_list[j] }
        daily_rep = requests.post(daily_url,headers=access_header('json'),data=json.dumps(datas))
        if daily_rep.status_code == 200:
            print(org_list[i],name_list[i],customer_name_list[j],"返回正常",daily_rep.json()['data'])
        else:
            print(orgid[i],name_list[i],customer_name_list[j],"返回报错",daily_rep.content)

