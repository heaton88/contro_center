# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/30 9:09 上午
# _FileName_: single_interface.py

import requests
import json
from config_control import login,access_header

interface_url = 'http://k8sdev.golowo.com/g3-screen-web/manageCenter/queryProjectStatics'
payload = {"orgCode": "-6944734322880132047,0100000000",
           "customerCode": "",
           "groupLevel": "province",
           "type": "china"}


interface_rep = requests.post(interface_url,data=json.dumps(payload),headers=access_header('json')).content
print(interface_rep)