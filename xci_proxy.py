#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-20 21:02:52
# @Author  : caryangBingo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import re
import requests
#from bs4 import BeautifulSoup
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
XiCi_List = []
XiCi_Html = requests.get("http://www.yun-daili.com")
# print(XiCi_Html.text)
ip_list = r'style1">\b(.*?)</td'
ip_cont = r'style2">\b(.*?)</td'
ip_wnet = re.findall(ip_list, XiCi_Html.text, re.S | re.M)
ip_wcon = re.findall(ip_cont, XiCi_Html.text, re.S | re.M)
# print(ip_wcon)
# print(ip_wnet)
et = 0
for ip in ip_wnet:
    i = re.sub(',', '\n', ip)
    XiCi_List.append(i.strip() + ':' + ip_wcon[et])
    print(i.strip())
    et += 1
print(XiCi_List)
