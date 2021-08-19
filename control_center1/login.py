# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/8/19 11:01 上午
# _FileName_: login.py

import json
import requests

def login():
    login_url = 'https://k8sdev.golowo.com/g3-authcenter-web/oauth/token'
    login_header = {
        'authorization': 'Basic ZzNwY2M6aXh1NHJNSUw=',
        'content-type': 'application/x-www-form-urlencoded'
    }
    login_data = 'username=zjsj2021&password=zjsjjt&grant_type=password&userType=screen'
    login_rep = requests.post(login_url,data=login_data,headers=login_header)
    access_token = login_rep.json()['access_token']
    refresh_token = login_rep.json()['refresh_token']
    userid = login_rep.json()['userId']
    orgid = login_rep.json()['orgId']
    return access_token,refresh_token,userid,orgid

print(login()[0])