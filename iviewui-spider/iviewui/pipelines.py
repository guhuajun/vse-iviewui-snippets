# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import simplejson as json

class IviewuiPipeline(object):
    snippets = []

    def open_spider(self, spider):
        self.file = open('items.json', 'w')

    def close_spider(self, spider):
        self.file.writelines(json.dumps(self.snippets, indent=4))
        self.file.close()

    def process_item(self, item, spider):
        self.snippets.append(dict(item))
        return item
