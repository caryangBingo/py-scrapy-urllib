# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import io
import json
from scrapy.exceptions import DropItem

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')


class CnblogspiderPipeline(object):
    def __init__(self):
        self.file = open('papers.json', 'wb')

    def process_item(self, item, spider):
        if item['title']:
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line.encode('utf-8'))
            return item
        else:
            raise DropItem("Missing title in %s" % item)
