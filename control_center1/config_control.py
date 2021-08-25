# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/29 9:18 上午
# _FileName_: config_control.py


import requests
import json

login_data = 'username=zjsj2021&password=zjsjjt&grant_type=password&userType=screen'
login_url = 'https://k8sdev.golowo.com/g3-authcenter-web/oauth/token'

def login_header(act):
    if act == 'form':
        form_header = {
            'authorization': 'Basic ZzNwY2M6aXh1NHJNSUw=',
            'content-type': 'application/x-www-form-urlencoded'
        }
        return form_header
    else:
        json_header = {
            'authorization': 'Basic ZzNwY2M6aXh1NHJNSUw=',
            'content-type': 'application/json'}
        return json_header


def login():
    login_rep = requests.post(login_url,data=login_data,headers=login_header('form'))
    access_token = login_rep.json()['access_token']
    refresh_token = login_rep.json()['refresh_token']
    userid = login_rep.json()['userId']
    orgid = login_rep.json()['orgId']
    return access_token,refresh_token,userid,orgid

access_token = login()[0]
refresh_token = login()[1]
userid = login()[2]
orgid = login()[3]

def access_header(act):
    if act == 'form':
        form_header = {
            'Accept': 'application/x-www-form-urlencoded, text/plain, */*',
            "Content-Type": "application/application/x-www-form-urlencoded;charset=UTF-8",
            'Authorization': 'bearer ' + access_token,
            'referer': 'https://k8sdev.golowo.com/g3-screen-frontend/',
            'user-agent': 'Chrome/92.0.4515.159'
        }
        return form_header
    else:
        json_header = {
            'Accept': 'application/json, text/plain, */*',
            "Content-Type": "application/json;charset=UTF-8",
            'Authorization': 'bearer ' + access_token,
            'referer': 'https://k8sdev.golowo.com/g3-screen-frontend/',
            'user-agent': 'Chrome/92.0.4515.159'
        }
        return json_header

def sj_list():
    org_url = 'http://k8sdev.golowo.com/g3-orgcenter-web/org/querySecondaryOrgTreeData?orgId='+orgid

    org_data = {'orgId':orgid}
    org_rep = requests.get(org_url,headers=access_header('json'),params=json.dumps(org_data))
    infolist = json.loads(org_rep.content)['data'][0]['children']

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

    return code_list,name_list,org_list
code_list = sj_list()[0]
name_list = sj_list()[1]
org_list = sj_list()[2]

#
#
def customer_list():
    customer_url = 'http://k8sdev.golowo.com/g3-enterprisecenter-web/customer/searchCustomerList'
    payload = {"size": 100000000}

    id_list = []
    code_list = []
    name_list = []
    customer_rep = requests.post(customer_url, data=json.dumps(payload), headers=access_header('json'))
    customer_json = json.loads(customer_rep.content)['data']['items']

    for i in range(0, len(customer_json)):
        id_list.append(customer_json[i]['id'])
        code_list.append(customer_json[i]['code'])
        name_list.append(customer_json[i]['name'])

    return id_list,code_list,name_list
