# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json, codecs


class MeijuPipeline(object):
    def process_item(self, item, spider):
        return item


class MeijuspiderPipeline(object):
    def __init__(self):
        self.file= codecs.open('meiju.json','w',encoding='utf-8')
    def process_itme(self,item,spider):
        #数据存储
        content = json.dumps(dict(item),ensure_ascii=False)
        self.file.write(content)

        return item
    def close_spider(self,spider):
        self.file.close()