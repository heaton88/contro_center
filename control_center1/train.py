# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/8/29 9:21 下午
# _FileName_: train.py

import requests
import json

#登录接口
login_url = 'https://k8sdev.golowo.com/g3-authcenter-web/oauth/token'
#登录参数
data1 = 'username=zjsj2021&password=zjsjjt&grant_type=password&userType=screen'
#登录请求头
api_header = {
	'content-type': 'application/x-www-form-urlencoded',
	'authorization': 'Basic ZzNwY2M6aXh1NHJNSUw='}

#登录接口返回值
login_response = requests.post(login_url,data=data1,headers=api_header)
#取token
train_token = login_response.json()['access_token']
#项目详情接口地址
project_url = 'https://k8sdev.golowo.com/g3-screen-web/manageCenter/queryProjectOperateDetail?orgCode=-6944734322880132047,0100000000&customerCode='
#项目详情接口地址请求头
project_header = {'authorization': 'bearer ' + train_token}
#项目详情接口请求参数
project_data = {'orgCode': "-6944734322880132047,0100000000&customerCode="}
#项目详情接口调用
project_details = requests.get(project_url,params=project_data,headers=project_header)
print(project_details.json()['data'])