#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date            : 2018-07-20 17:05:57
# @Author        : caryangBingo
# @Filename   : example.py
# @Software   : Sublime Text3

import scrapy


class CnblogsSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["cnblogs.com"]

    start_urls = [
        'http://www.cnblogs.com/qiyeboy/default.html?page=1',
    ]

    def parse(self, response):
        papers = response.xpath(".//*[@class='day']")

        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(
                ".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(
                ".//*[@class='postTitle']/a/text()").extract()[0]
            print(url, title, time, content)
