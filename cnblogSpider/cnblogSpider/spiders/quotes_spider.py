#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date            : 2018-07-20 17:05:57
# @Author        : caryangBingo
# @Filename   : example.py
# @Software   : Sublime Text3

import scrapy
import re
from scrapy import Selector
from cnblogSpider.items import CnblogspiderItem


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
            item = CnblogspiderItem(
                url=url, title=title, time=time, content=content)
            request = scrapy.Request(url, callback=self.parse_body)
            request.meta['item'] = item
            yield request
        next_page = Selector(response).re(u'<a href="(\\S*)">下一页</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)

    def parse_body(self, response):
        item = response.meta['item']
        body = response.xpath(".//*[@class='postBody']")
        item['cimage_urls'] = body.xpath('.//img//@src').extract()
        yield item
