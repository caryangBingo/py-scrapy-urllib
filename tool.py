#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-18 16:25:37
# @Author  : caryangBingo (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import re

# 处理页面标签类


class Tool:
    # 去除img标签,1-7位空格,
    removeImg = re.compile(r'<img.*?>| {1,7}| ')
    # 删除超链接标签
    removeAddr = re.compile(r'<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile(r'<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile(r'<td>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile(r'<br><br>|<br>')
    # 将其余标签剔除r
    removeExtraTag = re.compile(r'<.*?>')
    # 将多行空行删除
    removeNoneLine = re.compile(r'\n+')
    # 删除 
    removeSpace = re.compile(r' ')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeNoneLine, "\n", x)
        x = re.sub(self.removeSpace, "", x)
        # strip()将前后多余内容删除
        return x.strip()
