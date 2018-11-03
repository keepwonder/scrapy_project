# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json', 'w', encoding='utf-8')
#
#     def open_spider(self, spider):
#         print('爬虫开始了...')
#
#     def process_item(self, item, spider):
#         item = dict(item)
#         item_json = json.dumps(item, ensure_ascii=False)
#         self.fp.write(item_json+'\n')
#         return item
#
#     def close_spider(self, spider):
#         print('爬虫结束了')
#         self.fp.close()

# from scrapy.exporters import JsonItemExporter
#
#
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json', 'wb')
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False)
#         self.exporter.start_exporting()
#
#     def open_spider(self, spider):
#         print('爬虫开始了...')
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         print('爬虫结束了')
#         self.exporter.finish_exporting()
#         self.fp.close()

from scrapy.exporters import JsonLinesItemExporter


class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('duanzi.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False)

    def open_spider(self, spider):
        print('爬虫开始了...')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        print('爬虫结束了...')
        self.fp.close()