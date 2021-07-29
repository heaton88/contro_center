# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/7 9:41 上午
# _FileName_: sj_contract.py


import requests
import json


org_url = 'http://k8sdev.golowo.com/g3-orgcenter-web/org/querySecondaryOrgTreeData'

infolist = json.loads(requests.get(org_url).content)['data'][0]['children']
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
    year_status = requests.get(sign_url).status_code
    if year_status != 200:
        print(name_list[j],"接口报错")
    else:
        yearamount = json.loads(requests.get(sign_url).content)['data']['yearAmount']
        monthamount = json.loads(requests.get(sign_url).content)['data']['monthAmount']
        print(name_list[j],yearamount)
        year_list.append(yearamount)
        month_list.append(monthamount)
total_company = sum(year_list)
print(total_company)


sj_url_total = 'http://k8sdev.golowo.com/g3-screen-web/manageCenter/queryContractAmount?orgCode=-6944734322880132047,0100000000&customerCode='
sj_response_year = json.loads(requests.get(sj_url_total).content)['data']['yearAmount']
sj_response_month = json.loads(requests.get(sj_url_total).content)['data']['monthAmount']
print(sj_response_year)
print(sum(month_list))
print(sj_response_month)

