# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/7/29 9:18 上午
# _FileName_: sj_interface.py

from config_control import sj_list
import requests

code_list = sj_list()[0]
name_list = sj_list()[1]
org_list = sj_list()[2]

rep_list = []

class Get_url:
    def __init__(self,sjurl):
        self.sjurl = sjurl
        for i in range(len(code_list)):
            outputvalue_rank_url = self.sjurl+org_list[i]+','+code_list[i]+'&customerCode='
            outputvalue_rank_url_rep = requests.get(outputvalue_rank_url).status_code
            outputvalue_rank_url_con = requests.get(outputvalue_rank_url).content
            if outputvalue_rank_url_rep != 200:
                print(outputvalue_rank_url_con)
                print(i+1,name_list[i],"接口报错")
            else:
                rep_list.append(outputvalue_rank_url_rep)
                print(i+1,name_list[i],"接口正常")
        print(len(rep_list))


Get_url('http://k8sdev.golowo.com/g3-screen-web/manageCenter/queryOutputValuePercentage?orgCode=')