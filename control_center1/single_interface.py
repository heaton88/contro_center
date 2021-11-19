# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/30 9:09 上午
# _FileName_: single_interface.py

import requests
import json
from config_control import access_header,login_screen

login_screen()

interface_url = 'http://k8stest.golowo.com/g3-antiepidemic-web/statichealth/queryProjectReportPercent'
project_info = []
records_list = []
project_id = []
for i in range(1,5):
    payload = {
        "orgId": "-6944734322880132047",
        "pageReq": {
                "pageSize": 500,
                "pageNumber": i
                        },
        "createtime": '2021-09-23'
    }

    interface_rep = requests.post(interface_url,data=json.dumps(payload),headers=access_header('json'))
    records_info = interface_rep.json()['data']['records']
    for j in range(0,len(records_list)):
        project_id.append(records_info[j]['projectId'])
print(project_id)