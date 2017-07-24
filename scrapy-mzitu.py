#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-18 23:00:58
# @Author  : caryangBingo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import io
import os
import re
import sys
import datetime
from bs4 import BeautifulSoup
from pxydowwload import request
from pymongo import MongoClient

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class mzitu():
    def __init__(self):
        client = MongoClient('192.168.225.115', 27017)
        db = client["mzitulg"]
        self.mzitu_collection = db["mzitulg"]
        self.title = ''
        self.url = ''
        self.img_urls = []  # 初始化一个 列表 用来保存图片地址

    def all_url(self, url):
        html = request.get_agent(url, 3)
        # html = self.request(url)  # 调用request函数把套图地址传进去会返回给我们一个response
        all_a = BeautifulSoup(html.text, 'lxml').find(
            'div', class_='postlist').find_all('a')[0:47]
        # print(len(all_a))
        for i in range(1, len(all_a) - 1, 2):
            a = all_a[i]
            title = a.get_text()
            self.title = title
            print(u'开始保存：', title)  # 加点提示不然太枯燥了
            # 我注意到有个标题带有 ？  这个符号Windows系统是不能创建文件夹的所以要替换掉
            path = str(title).replace("?", '_')
            self.mkdir(path)  # 调用mkdir函数创建文件夹！这儿path代表的是标题title哦！！！！！不要糊涂了哦！
            #os.chdir("/Users/Caryang/Pictures/mzitu.com/" + path)
            href = a['href']
            # 调用html函数把href参数传递过去！href是啥还记的吧？ 就是套图的地址哦！！不要迷糊了哦！
            self.url = href  # 将页面地址保存到self.url中
            if self.mzitu_collection.find_one({'主题页面地址': href}):
                print(u'这个页面已经爬取过！')
            else:
                self.html(href)

    def html(self, href):  # 这个函数是处理套图地址获得图片的页面地址
        html = request.get_agent(href, 3)
        #html = self.request(href)
        max_span = BeautifulSoup(html.text, 'lxml').find_all('span')[
            8].get_text()
        page_num = 0
        for page in range(1, int(max_span) + 1):
            page_num += 1
            page_url = href + '/' + str(page)
            # 调用img函数,把上面我们我们需要的两个变量，传递给下一个函数。
            self.img(page_url, max_span, page_num)

    def img(self, page_url, max_span, page_num):  # 这个函数处理图片页面地址获得图片的实际地址
        img_html = request.get_agent(page_url, 3)
        #img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find(
            'div', class_='main-image').find('img')['src']
        self.save(img_url)
        self.img_urls.append(img_url)

        if int(max_span) == page_num:
            self.save(img_url)
            post = {  # 这是构造一个字典，里面有啥都是中文，很好理解吧！
                '主题页面标题': self.title,
                '主题页面地址': self.url,
                '主题图片地址': self.img_urls,
                '主题获取时间': datetime.datetime.now()
            }
            self.mzitu_collection.save(post)
            print(u'插入数据库成功!')
        else:
            self.save(img_url)

    def save(self, img_url):  # 这个函数保存图片
        name = img_url[-9:-4]
        print(u'开始保存：', img_url)
        img = request.get_agent(img_url, 3)
        #img = self.request(img_url)
        fp = open(name + '.jpg', 'ab')
        fp.write(img.content)
        fp.close()

    def mkdir(self, path):  # 这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join(
            "/Users/Caryang/Pictures/mzitu.com", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join(
                "/Users/Caryang/Pictures/mzitu.com", path))
            os.chdir(os.path.join("/Users/Caryang/Pictures/mzitu.com", path))
            # # 切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            os.chdir(os.path.join("/Users/Caryang/Pictures/mzitu.com", path))
            return False

    """
    def request(self, url):  # 这个函数获取网页的response 然后返回
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers)
        return content
    """


Mzitu = mzitu()  # 实例化
# 给函数all_url传入参数  你可以当作启动爬虫（就是入口）
Mzitu.all_url('http://www.mzitu.com/xinggan')
