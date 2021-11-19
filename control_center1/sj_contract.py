# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/7 9:41 上午
# _FileName_: sj_contract.py


import requests
import json
from config_control import *


org_url = 'http://k8stest.golowo.com/g3-orgcenter-web/org/querySecondaryOrgTreeData'

infolist = json.loads(requests.get(org_url,headers=access_header('json')).content)['data'][0]['children']
code_list = []
name_list = []
org_list = []

for i in range(0,len(infolist)):
    codes = infolist[i]['code']
    names = infolist[i]['name']
    orgs = infolist[i]['id']
    code_list.append(codes)
    name_list.append(names)
    org_list.append(orgs)


sign_list = []
year_list = []
month_list = []

for j in range(0,len(code_list)):
    sign_url = 'http://k8sdev.golowo.com/g3-screen-web/manageCenter/queryContractAmount?orgCode='+org_list[j]+','+code_list[j]+'&customerCode='
    year_status = requests.get(sign_url,headers=access_header('json')).status_code

    if year_status != 200:
        print(name_list[j],"接口报错")
    else:
        data_status = json.loads(requests.get(sign_url,headers=access_header('json')).content)['data']['monthAmountDataVoList']
        datas_status = json.loads(requests.get(sign_url,headers=access_header('json')).content)['data']
        if data_status != []:
            yearamount = datas_status['yearAmount']
            monthamount = datas_status['monthAmount']
            print(name_list[j],yearamount)
            year_list.append(yearamount)
            month_list.append(monthamount)
        else:
            print(name_list[j],code_list[j],"data为空")
total_company = sum(year_list)
print(total_company)


