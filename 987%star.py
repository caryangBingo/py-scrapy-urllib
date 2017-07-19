#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-19 20:35:17
# @Author  : caryangBingo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import io
import os
import sys
import requests
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class pf_photo(object):
    """docstring for star_photo_url"""

    def star_photo_url(self, xStar_url, home_url):
        title = 0
        start_html = self.requests(xStar_url)
        post_Soup = BeautifulSoup(start_html.text, 'lxml')
        list_url = post_Soup.find('div', class_='con_list').find_all('a')
        for lts in list_url:
            # title = lts.get_text().encode('utf-8')
            title += 1
            print(u'开始保存第%s个妹子：' % title)
            #.encode('utf-8').decode('utf-8')
            # path = str(title).replace("?", '_')
            path = str(title)
            self.mkdir_photo(path)
            href = lts['href']
            page_img_url = home_url + href
            with open('%s.txt' % title, 'w+') as fp:
                fp.write(page_img_url)
                fp.close()
            # print(u'这是第%s个star:' % title, img_url)
            self.post_img(page_img_url)

        #   get_title = html_Soup.find(
        #       'div', class_='con_nrong').find('h1').get_text()
        #   print(get_title)
        # print(get_img_url)

    # 函数：处理图片页面地址获得图片的实际地址

    def post_img(self, img_url):
        i_name = 0
        html = self.requests(img_url)
        html_Soup = BeautifulSoup(html.text, 'lxml')
        get_img_urls = html_Soup.find(
            'div', class_='nrong').find_all('img')
        for get_img_index in get_img_urls:
            if i_name <= len(get_img_urls):
                i_name += 1
                self.img_save(get_img_index, i_name)
            else:
                pass

    # 函数：保存图片文件

    def img_save(self, image_url, i_name):
        # img_name = image_url[-8:-3]
        img_name = 'img''%s' % i_name
        get_img = self.requests(image_url['src'])
        fp = open(img_name + '.jpg', 'ab')
        fp.write(get_img.content)
        fp.close()

    # 函数：创建文件存储目录路径：path
    def mkdir_photo(self, path):
        isExists = os.path.exists(os.path.join(
            "/Users/Caryang/Pictures/mzitu.com", path))
        if not isExists:
            print(u'建了一个名字为：', path, u'的妹子文件目录')
            os.makedirs(os.path.join(
                "/Users/Caryang/Pictures/mzitu.com", path))
            os.chdir(os.path.join(
                "/Users/Caryang/Pictures/mzitu.com", path))  # 切换目录
            return True
        else:
            print(u'名字为', path, u'的妹子目录已存在!')
            return False

    # 函数：从load_url获取网页的response，然后返回
    def requests(self, load_url):
        headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,en-GB;q=0.2',
                   'Cache-Control': 'max-age=0',
                   'Connection': 'keep-alive',
                   #'Cookie': 'UM_distinctid=15d5acc35c432a-082891f1216a65-3066780a-13c680-15d5acc35c6663; CNZZDATA5735278=cnzz_eid%3D1574989250-1500462223-%26ntime%3D1500462223'
                   }
        content = requests.get(load_url, headers=headers)
   %     return content

pf_photo = pf_photo()
home_url = ''
xStar_url = ''
pf_photo.star_photo_url(
    xStar_url, home_url)

# print("\n第一步保存信息完成，输入y保存所有图片，其他信息退出：")
