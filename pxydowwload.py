#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-21 22:09:29
# @Author  : caryangBingo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import io
import os
import re
import sys
import requests
import random
import time

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='iso-8859-1')


class meizi_load():
    def __init__(self):

        self.XiCi_List = []
        XiCi_Html = requests.get("http://www.yun-daili.com")
        # print(XiCi_Html.text)
        ip_list = r'style[1,2]">\b(.*?)</td'
        ip_style = re.findall(ip_list, XiCi_Html.text, re.S)
        # ip_wcon = re.findall(ip_cont, XiCi_Html.text, re.S)
        # print(ip_style)
        for ip_count in range(0, len(ip_style) - 1, 2):
            ip_net = ip_style[ip_count]
            ip_con = ip_style[ip_count + 1]
            self.XiCi_List.append(ip_net + ':' + ip_con)

        self.brower_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

    def get_agent(self, her_url, timeout, proxy=None, num_retries=3):
        #print(u'开始获取：', her_url)
        Brower_UA = random.choice(self.brower_agent_list)
        headers = {"User-Agent": Brower_UA}
        if proxy == None:
            try:
                return requests.get(her_url, headers=headers, timeout=timeout)
            except:
                if num_retries > 0:
                    time.sleep(10)
                    print(u'获取网页出错，10s后获取倒数第：', num_retries, u'次')
                    return self.get_agent(her_url, timeout, num_retries - 1)
                else:
                    print(u'开始使用代理')
                    time.sleep(10)
                    use_ip = ''.join(
                        str(random.choice(self.XiCi_List)).strip())
                    proxy = {'http': use_ip}
                    return self.get_agent(her_url, timeout, proxy,)
            #response = requests.get(her_url, headers=headers)
            # print(response)
            # return response
        else:
            try:
                use_ip = ''.join(str(random.choice(self.XiCi_List)).strip())
                proxy = {'http': use_ip}
                return requests.get(her_url, headers=headers, proxies=proxy, timeout=timeout)
            except:
                if num_retries > 0:
                    time.sleep(10)
                    use_ip = ''.join(
                        str(random.choice(self.XiCi_List)).strip())
                    proxy = {'http': use_ip}
                    print(u'获取网页出错，10s后获取倒数第：', num_retries, u'次')
                    print('当前代理是：', proxy)
                    return self.get_agent(her_url, timeout, proxy, num_retries - 1)
                else:
                    print('代理也不好使了！取消代理！！')
                    return self.get_agent(her_url, 3)
            #    response = requests.get(her_url, headers=headers, proxies=proxy)
            #    return response
#Xz = meizi_load()
#her_url = "http://www.baidu.com"
#print(Xz.get_agent((her_url), 3))
request = meizi_load()
