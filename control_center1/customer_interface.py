# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/29 10:55 上午
# _FileName_: customer_interface.py

from config_control import customer_list,sj_list,login,acess_header
import requests

id_list = customer_list()[0]
name_list = customer_list()[2]
code1_list = customer_list()[1]
access_token = login()[0]
refresh_token = login()[1]
userid = login()[2]
orgid = login()[3]



org_list = sj_list()[2]
code_list = sj_list()[0]

rep_list = []

class Customer_url:
    def __init__(self,customer_url):
        self.customer_url = customer_url
        for i in range(len(code1_list)):
            outputvalue_rank_url = self.customer_url+org_list[0]+','+code_list[0]+'&customerCode='+id_list[i]+','+code1_list[i]
            outputvalue_rank_url_rep = requests.get(outputvalue_rank_url,headers=acess_header('form')).status_code
            outputvalue_rank_url_con = requests.get(outputvalue_rank_url).content
            if outputvalue_rank_url_rep != 200:
                print(outputvalue_rank_url_con)
                print(i+1,name_list[i],"接口报错")
            else:
                rep_list.append(outputvalue_rank_url_rep)
                print(i+1,name_list[i],"接口正常")
        print(len(rep_list))

Customer_url('http://k8sdev.golowo.com/g3-screen-web/manageCenter/queryContractAmount?orgCode=')