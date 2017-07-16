#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-16 22:47:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
import ssl
import urllib.request
from importlib import reload

#第一个爬虫练习
"""
url= "http://www.baidu.com"
data = urllib.request.urlopen(url).read()#
#data = data.decode('UTF-8')
print (data)
"""

url = "http://www.douban.com/"
request = urllib.request.Request(url)
ssl._create_default_https_context = ssl._create_unverified_context
responseurl = urllib.request.urlopen(request)
data = responseurl.read()
#data = data.decode('utf-8')
print(data)