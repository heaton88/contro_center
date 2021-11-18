# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/11/18 9:41 上午
# _FileName_: synchronization_data.py

#指挥大屏防疫实时巡检数据更新
import requests
import time
from config_control import login_screeen,access_header,sync_url


sync_date = 'date' + '=' + time.strftime("%Y-%m-%d", time.localtime())

access_token = login_screeen()[0]

syn_url = sync_url + sync_date
syn_rq = requests.get(syn_url,headers=access_header('json'))
print(syn_rq.text)