# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/29 9:18 上午
# _FileName_: config_control.py


import requests
import json

def sj_list():
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
    # print(code_list)
    # print(name_list)
    # print(org_list)
    return code_list,name_list,org_list


def customer_list():
    customer_url = 'http://k8sdev.golowo.com/g3-enterprisecenter-web/customer/searchCustomerList'
    payload = {"size": 100000000}
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json;charset=UTF-8",
    }
    id_list = []
    code_list = []
    name_list = []
    customer_rep = requests.post(customer_url, data=json.dumps(payload), headers=headers)
    customer_json = json.loads(customer_rep.content)['data']['items']

    for i in range(0, len(customer_json)):
        id_list.append(customer_json[i]['id'])
        code_list.append(customer_json[i]['code'])
        name_list.append(customer_json[i]['name'])
    print(id_list)
    print(name_list)
    print(code_list)
    return id_list,code_list,name_list
