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
ip_list = r'style[1,2]">\b(.*?)</td'
#ip_cont = r'style2">\b(.*?)</td'
ip_style = re.findall(ip_list, XiCi_Html.text, re.S)
#ip_wcon = re.findall(ip_cont, XiCi_Html.text, re.S)
# print(ip_style)
for ip_count in range(0, len(ip_style), 2):
    ip_net = ip_style[ip_count]
    ip_con = ip_style[ip_count + 1]
    XiCi_List.append(ip_net + ':' + ip_con)
print(XiCi_List)
# print(ip_wcon)
"""
et = 0
for ip in ip_wnet[range(1, len(ip_wnet), 2)]:
    #i = re.sub('', '', ip)
    XiCi_List.append(ip)
    print(i.strip())
    et += 1
print(XiCi_List)
"""
