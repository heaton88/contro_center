# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/11/16 7:17 下午
# _FileName_: add_new_project.py

import json
import requests
from control_center1.config_control import login_screeen,access_header,access_token

login_screeen()
refresh_token = login_screeen()[1]
userid = login_screeen()[2]
orgid = login_screeen()[3]

add_project_url = 'http://k8stest.golowo.com/g3-projectcenter-web/project/insert'
payload = {
    "secondaryOrgId":"-5085243703379410284",
    "constructOrgName":"第一建设工程有限责任公司华东公司",
    "constructModel":"工程总承包",
    "projectCode":20190304314,
    "projectName":"测试专用1116",
    "constructOrgId":"-2186182769703304181",
    "shortName":"测试专用",
    "enginerCategory":"基础设施",
    "enginerCategory2":"交通运输工程",
    "enginerCategory3":"公路",
    "enginerCategory4":"公路",
    "projectStateName":"在施阶段",
    "projectType":"project",
    "gclx":"xxgc",
    "country":"中国",
    "district":"江汉区",
    "address":"湖北省武汉市江汉区汉兴街街道双华路大兴第一实验小学(新华家园校区)",
    "addressLng":114.262866,"addressLat":30.624543,
    "tenantid":"cscec3b"
}

add_project_rep = requests.post(add_project_url,headers=access_header('json'),data=json.dumps(payload))
print(add_project_rep.text)