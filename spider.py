#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-18 16:24:47
# @Author  : caryangBingo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import urllib.request
import re
import tool
import os
import http.cookiejar

# 抓取MM


class Spider:

    # 页面初始化
    def __init__(self):
        self.siteURL = 'https://mm.taobao.com/search_tstar_model.htm'
        self.tool = tool.Tool()

    # 获取索引页面的内容
    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        return response.read().decode('gbk')

    # 获取索引界面所有MM的信息，list格式
    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile(
            '<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            contents.append([item[0], item[1], item[2], item[3], item[4]])
        return contents

    # 获取MM个人详情页面
    def getDetailPage(self, infoURL):
        def makeMyOpener(head={
                'accept-encoding': 'deflate, sdch',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                # 此处填写浏览器发送的cookie数据，开发者模式可捕获
                'cookie': 'thw=cn; v=0; _tb_token_=ed3e537eee38e; uc3=sg2=AVUmfqNnWoGPGTJ4gENbfZpe%2FkbplGialS%2FlXfLU08k%3D&nk2=rUePjBPFcJ1Zrg%3D%3D&id2=UoYdVU3Lb0nB&vt3=F8dBzWIGOl7d%2BZ7Huw0%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; hng=CN%7Czh-cn%7CCNY; existShop=MTUwMDM2MDkwOQ%3D%3D; uss=AQYMPMd%2Fgu%2FdNnHcM9Cck94ecGXngi%2FSNj2ivY6jAYSJkWJDREv1jnCt; lgc=%5Cu65E0%5Cu60C5sv%5Cu6E29%5Cu67D4; tracknick=%5Cu65E0%5Cu60C5sv%5Cu6E29%5Cu67D4; skt=d68cfa4bb9340384; publishItemObj=Ng%3D%3D; _cc_=Vq8l%2BKCLiw%3D%3D; tg=0; mt=ci=0_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; whl=-1%260%260%261500361082762; cookie2=10863069964cb17db9cda91427d47e70; t=43b75585f7c1257a4a553d3c9647eaa1; cna=; JSESSIONID=928FD6C2A2B4AD512C246E03B1060B5C; uc1=cookie14=UoTcDzH4%2Be4stQ%3D%3D; isg=AnV1INOGQFmuPKTvZ7zvm_3yhPHvWiPCg88wb_eadOwxzpXAv0I51INOZKSD',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
        }):
            cookie = http.cookiejar.CookieJar()
            opener = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor(cookie))
            header = []
            for key, value in head.items():
                elem = (key, value)
                header.append(elem)
            opener.addheaders = header
            return opener

        oper = makeMyOpener()
        uop = oper.open(infoURL)
        data = uop.read().decode('gbk')
        return data
        # response = urllib.request.urlopen(infoURL)
        # return response.read().decode('gbk')

    # 获取个人文字简介
    def getBrief(self, page):
        pattern = re.compile(
            '<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
        result = re.search(pattern, page)
        # print(result.group())
        return self.tool.replace(result.group(1))

    # 获取页面所有图片
    def getAllImg(self, page):
        pattern = re.compile(
            '<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
        # 个人信息页面所有代码
        content = re.search(pattern, page)
        # 从代码中提取图片
        patternImg = re.compile('<img.*?src="(.*?)"', re.S)
        images = re.findall(patternImg, content.group(1))
        return images

    # 保存多张写真图片
    def saveImgs(self, images, name):
        number = 1
        print(u"发现", name, u"共有", len(images), u"张照片")
        for imageURL in images:
            splitPath = imageURL.split('.')
            splitPath = splitPath
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = name + "/" + str(number) + "." + fTail
            imageURL = 'https:' + imageURL
            self.saveImg(imageURL, fileName)
            number += 1

    # 保存头像
    def saveIcon(self, iconURL, name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + "/icon." + fTail
        self.saveImg(iconURL, fileName)

    # 保存个人简介
    def saveBrief(self, content, name):
        fileName = name + "/" + name + ".txt"
        f = open(fileName, "w+")
        print(u"正在保存信息为", fileName)
        f.write(content.decode('utf-8'))

    # 保存图片地址页到各文件夹中
    def saveToLocal(self, Li, name):
        fileName = name + "/" + "urlPage.txt"
        print(u"正在保存图片地址页：", fileName)
        # f.write(content.decode('utf-8'))
        # pre=pre.replace("[","")
        # pre=pre.replace("]","")+"\n"
        #print (pre)
        f = open(fileName, "w")
        f.write(Li)
        f.close()

        # 追加方式写入当前爬行的名字，后续调用
        content = name + " "
        with open('url.txt', 'a') as url:
            url.write(content)
            url.close()
        print(name + u"追加完成！\n")

    # 传入图片地址，文件名，保存单张图片
    def saveImg(self, imageURL, fileName):
        try:
            u = urllib.request.urlopen(imageURL)
            data = u.read()
            f = open(fileName, 'wb')
            f.write(data)
            print(u"正在保存的一张图片为", fileName)
            f.close()
        except urllib.request.URLError as e:
            print(e.reason)

    # 创建新目录
    def mkdir(self, path):
        path = path.strip()
        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            print(u"新建了名字叫做", path, u'的文件夹')
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(u"名为", path, '的文件夹已经创建成功')
            return False

    # 将一页淘宝MM的信息保存起来
    def savePageInfo(self, pageIndex):
        # 获取第一页淘宝MM列表
        contents = self.getContents(pageIndex)
        for item in contents:
            # item[0]个人详情URL,item[1]头像URL,item[2]姓名,item[3]年龄,item[4]居住地
            print(u"发现一位名字叫", item[2], u"年龄", item[3], u",她在", item[4])
            print(u"正在保存", item[2], "的信息")

            print(u"个人详情地址是", "https:" + str(item[0]))
            # 个人详情页面的URL
            detailURL = "http:" + str(item[0])
            # 得到个人详情页面代码
            detailPage = self.getDetailPage(detailURL)
            # 获取个人简介
            brief = self.getBrief(detailPage)
            # 获取所有图片列表
            images = self.getAllImg(detailPage)
            self.mkdir(item[2])
            # 保存个人简介
            self.saveBrief(brief.encode('utf-8'), item[2])
            # 保存图片地址页到本地
            self.saveToLocal(detailPage, item[2])
            # 保存头像
            self.saveIcon("https:" + str(item[1]), item[2])

    # 删除旧名单(如果有)
    def deleteOldTxt(self):
        filename = 'url.txt'
        if os.path.exists(filename):
            os.remove(filename)
            print("\n发现旧名单，已删除\n采集开始\n")

    # 传入起止页码，获取MM页面保存
    def savePagesInfo(self, start, end):
        for i in range(start, end + 1):
            print(u"正在寻找第", i, u"个地方")
            self.savePageInfo(i)
            # 保存图片
            # self.saveImgs(images,item[2])

    # 读取名字list
    def openNameList(self):
        with open("url.txt", "r") as f:
            for line in f:
                line = line.strip()
                # line.split(",")
                # result.append(line)
                # result.append(line.split(","))
            #\s匹配空格与tab，\s+表示至少一个
            result = re.split(r'\s+', line)
        return result

    # 逐个调取文件夹下页面中地址来保存
    def saveAll(self):
        i = spider.openNameList()
        for name in i:
            print("当前正在保存的是" + name + "的图片")
            filepath = name + "/urlPage.txt"
            with open(filepath, "r") as urlContent:
                urlContent = urlContent.read()
            images = spider.getAllImg(urlContent)
            spider.saveImgs(images, name)


# 传入起止页码即可，在此传入了6,10,表示抓取第6到10页的MM
spider = Spider()
spider.deleteOldTxt()
spider.savePagesInfo(1, 5)
print("\n第一步保存信息完成，输入y保存所有图片，其他信息退出：")
a = input()
if a == 'y':
    spider.saveAll()
else:
    pass