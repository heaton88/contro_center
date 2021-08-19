# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/30 9:54 上午
# _FileName_: test.py

import requests
import json

def request_methods(method,url):
    if method == 'get':
        request_method = requests.get(url)
    if method == 'post':
        request_method = requests.post(url)
    return request_method

# print(request_methods('get','http://yapi.golowo.com/mock/122/g3-screen-web/manageCenter/queryProjectStatics').content)
class Interface_request(object):
    def __init__(self,):
payload = {"orgCode":"-6944734322880132047,0100000000","customerCode":"","groupLevel":"province","type":"china"}
header_type = {"Content-Type": "application/json;charset=UTF-8"}

test = requests.get('http://k8sdev.golowo.com/g3-screen-web/manageCenter/queryProjectStatics',data=json.dumps(payload),headers=header_type)
print(test.text)
# class InterFace_test(object):
#     def __init__(self,resquestmethod,url):
#         self.requestmethod = resquest_method(url)
#     def request_method(self,request_type):
#         if request_type == 'get':
#             self.data_type == 'params'
#
#             return requests.get()
