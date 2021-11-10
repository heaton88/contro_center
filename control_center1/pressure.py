# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/9/24 9:41 上午
# _FileName_: pressure.py

import requests
import json
from config_control import login,access_header

project_id = []
records_info = []
reponse_list = []
time_list = []

interface_url = 'http://k8sdev.golowo.com/g3-antiepidemic-web/statichealth/queryProjectReportPercent'
for j in range(1,5):
    payload = {
            "orgId": "-6944734322880132047",
            "pageReq": {
                "pageSize": 2000,
                "pageNumber": j
                        },
           "createtime": '2021-09-23'
        }
    interface_rep = requests.post(interface_url,data=json.dumps(payload),headers=access_header('json'))
    for i in range(0,len(interface_rep.json()['data']['records'])):
        project_id.append(interface_rep.json()['data']['records'][i]['projectId'])
print(len(project_id))
print(project_id)

for l in range(0,len(project_id)):
    check_url = 'https://k8sdev.golowo.com/g3-antiepidemic-web/healthinfo/getHealthAndGuard?projectId=' + project_id[l]

    reponse_list.append(requests.get(check_url).elapsed.total_seconds())
    response_time = requests.get(check_url).elapsed
    print(response_time.total_seconds(),l)
    if response_time.total_seconds() > 0.3:
        print(response_time.total_seconds(),l)
        time_list.append(response_time.total_seconds())
posion = reponse_list.index(max(reponse_list),0)
print(max(reponse_list),posion)
print(time_list)
