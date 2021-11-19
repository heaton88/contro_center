# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/29 10:55 上午
# _FileName_: customer_interface.py

from config_control import *
import requests
import json


rep_list = []

class Customer_url:
    def __init__(self,customer_url):
        self.customer_url = customer_url
        for i in range(len(customer_code_list)):
            outputvalue_rank_url = self.customer_url+orgid+','+orgid +'&customerCode='+ customer_id_list[i] +','+ customer_code_list[i]
            outputvalue_rank_url_rep = requests.get(outputvalue_rank_url,headers=access_header('form')).status_code
            outputvalue_rank_url_con = requests.get(outputvalue_rank_url).content
            if outputvalue_rank_url_rep != 200:
                print(outputvalue_rank_url_con)
                print(i+1,customer_name_list[i],"接口报错")
            else:
                rep_list.append(outputvalue_rank_url_rep)
                print(i+1,customer_name_list[i],"接口正常")
        print(len(rep_list))

Customer_url('http://k8sdev.golowo.com/g3-screen-web/manageCenter/queryContractAmount?orgCode=')