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
    login_data = 'username=13332201206&password=123456&grant_type=password&userType=labormng'
    login_rep = requests.post(login_url,data=login_data,headers=login_header)
    access_token = login_rep.json()['access_token']
    refresh_token = login_rep.json()['refresh_token']
    userid = login_rep.json()['userId']
    orgid = login_rep.json()['orgId']
    return access_token,refresh_token,userid,orgid

print(login()[0])

api_url = 'https://k8sdev.golowo.com/g3-projectcenter-web/project/queryList'
api_header = {
    'content-type': 'application/json;charset=UTF-8',
    'authorization': 'Bearer ' + login()[0]
              }
payload = {
    "pageNumber":0,
    "pageSize":10,
    "condition":
        [
            {"field":"dr",
             "compare":"EQ",
             "data":717223234137050373
             }
        ],
    "sort":
        [
            {
                "field":"createtime",
                "sort":"desc"
            }
        ]
}

api_response = requests.post(api_url,headers=api_header,data=json.dumps(payload))
print(api_response.content)
