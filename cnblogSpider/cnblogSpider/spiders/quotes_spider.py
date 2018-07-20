#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date            : 2018-07-20 17:05:57
# @Author        : caryangBingo
# @Filename   : example.py
# @Software   : Sublime Text3

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as fp:
            fp.write(response.body)
        self.log('Saved file %s' % filename)
