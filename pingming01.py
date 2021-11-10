# -*- coding: utf-8 -*-
# _author_: heaton
# _date_: 2021/9/16 5:28 下午
# _FileName_: pingming01.py

import json
import requests

url = 'https://zjsj-test-open.pinming.org/sso/sso/login/jsonp.do?userName=42494&password=e10adc3949ba59abbe56e057f20f883e&appKey=8a9ca3205bb50be7015bb50be74a0000'
access_header = {

}

rep = requests.get(url)
print(rep.content)