# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/29 9:18 上午
# _FileName_: config_control.py


import requests
import json

#登录账号及密码
login_data = 'username=13332201206&password=123456&grant_type=password&userType=labormng'
#获取token接口链接
login_url = 'https://k8stest.golowo.com/g3-authcenter-web/oauth/token'
#指挥大屏防疫实时数据--健康上报同步数据接口
sync_url = 'https://k8stest.golowo.com/g3-antiepidemic-web/statichealth/trigger?'

#登录接口所需header
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

#登录获取token,refresh token 以及用户id和组织id
def login_screen():
    login_rep = requests.post(login_url, data=login_data, headers=login_header('form'))
    global access_token
    access_token = login_rep.json()['access_token']
    global refresh_token
    refresh_token = login_rep.json()['refresh_token']
    global userid
    userid = login_rep.json()['userId']
    global orgid
    orgid = login_rep.json()['orgId']
    # return access_token,refresh_token,userid,orgid

login_screen()

#获取token后，其他接口测试的header，内置登录后的token，后续调取api直接使用。
def access_header(act):
    if act == 'form':
        form_header = {
            'Accept': 'application/x-www-form-urlencoded, text/plain, */*',
            "Content-Type": "application/application/x-www-form-urlencoded;charset=UTF-8",
            'Authorization': 'bearer ' + access_token,
            'referer': 'https://k8stest.golowo.com/g3-screen-frontend/',
            'user-agent': 'Chrome/92.0.4515.159'
        }
        return form_header
    else:
        json_header = {
            'Accept': 'application/json, text/plain, */*',
            "Content-Type": "application/json;charset=UTF-8",
            'Authorization': 'bearer ' + access_token,
            'referer': 'https://k8stest.golowo.com/g3-screen-frontend/',
            'user-agent': 'Chrome/92.0.4515.159'
        }
        return json_header

#获取三局所有分公司的组织id及组织code
def sj_list():
    org_url = 'http://k8stest.golowo.com/g3-orgcenter-web/org/querySecondaryOrgTreeData?orgId='+orgid
    org_data = {'orgId':orgid}
    org_rep = requests.get(org_url,headers=access_header('json'),params=json.dumps(org_data))
    print(org_rep.json())
    global infolist
    infolist = json.loads(org_rep.content)['data'][0]['children']
    global code_list
    code_list = []
    global name_list
    name_list = []
    global org_list
    org_list = []

    # for i in range(0,len(infolist)):
    #     codes = infolist[i]['code']
    #     names = infolist[i]['name']
    #     orgs = infolist[i]['id']
    #     code_list.append(codes)
    #     name_list.append(names)
    #     org_list.append(orgs)

sj_list()

#
#获取三局级别所有客户列表信息（客户id及客户code）
def customer_list():
    customer_url = 'http://k8stest.golowo.com/g3-enterprisecenter-web/customer/searchCustomerList'
    payload = {"size": 100000000}
    global customer_id_list
    customer_id_list = []
    global customer_code_list
    customer_code_list = []
    global customer_name_list
    customer_name_list = []

    customer_rep = requests.post(customer_url, data=json.dumps(payload), headers=access_header('json'))
    customer_json = json.loads(customer_rep.content)['data']['items']

    for i in range(0, len(customer_json)):
        customer_id_list.append(customer_json[i]['id'])
        customer_code_list.append(customer_json[i]['code'])
        customer_name_list.append(customer_json[i]['name'])

customer_list()