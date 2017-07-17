#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: caryangBingo
# @Date:   2017-07-17 22:06:51
# @Last Modified by:   caryangBingo
# @Last Modified time: 2017-07-17 23:50:32

import os
import io
import sys
import re
import urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb2312')

"""
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,en-GB;q=0.2'
}
"""
def get_image(url):
    request = urllib.request.Request(url, headers=headers)
    # params = urllib.urlencode(post_params)
    responseurl = urllib.request.urlopen(request)
    get_img = responseurl.read()
    with open('001.jpg', 'wb') as fp:
        fp.write(get_img)
        print('图片下载完成')
    return

url = 'http://image.tianjimedia.com/uploadImages/2016/009/27/FW632S21L801.jpg'
get_image(url)

"""
# headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}


def download_page(url):
    # request = urllib.request.Request(url)
    request = urllib.request.Request(url, headers=headers)
    responseurl = urllib.request.urlopen(url)
    data = responseurl.read()
    # data = data.decode('gbk')
    return data


def get_image(html):
    regx = r'http://[\S]*\.jpg'
    pattern = re.compile(regx)
    get_img = re.findall(pattern, repr(html))
    num = 1
    for img in get_img:
        image = download_page(img)
        with open('%s.jpg' % num, 'wb') as fp:
            fp.write(image)
            num += 1
            # fp.close()
            print('正在下载第%s张图片' % num)
    return

url = 'http://pic.yesky.com/180/99839180_2.shtml'
html = download_page(url)
get_image(html)
