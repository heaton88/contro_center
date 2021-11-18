# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/11/16 7:53 下午
# _FileName_: add_sub.py

import json
import requests
from control_center1.config_control import login_screeen,access_header,access_token

login_screeen()
refresh_token = login_screeen()[1]
userid = login_screeen()[2]
orgid = login_screeen()[3]

add_sub_url = 'http://k8stest.golowo.com/g3-enterprisecenter-web/subcontractor/insert'

payload = {
        "address": "湖北省武汉市洪山区和平街道罗家港路",
        "addressLng": 114.366893,
        "addressLat": 30.601791,
        "areaCode": "420111",
        "city": "武汉市",
        "contractorType": "1001",
        "contractorTypeName": "物资供应类",
        "country": "中国",
        "creatorid": "f201eb07839e7d47dc0c1a8c0ac32bd8",
        "creator": "黄思维",
        "socialCreditNumber":'91210106MA0UMCE9XM',
        "subContractorName": "分包测试",
        "tenantid": "cscec3b",
        "enableState": 1,
        "province": "湖北省",
        "district": "洪山区"
}

add_sub_rep = requests.post(add_sub_url,headers=access_header('json'),data=json.dumps(payload))
print(add_sub_rep.text)