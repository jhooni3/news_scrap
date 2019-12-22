# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter, JsonItemExporter
from scrapy import signals

class CsvPipeline(object):
    def __init__(self):
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('%s_items.csv' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file)
        # self.exporter.fields_to_export = ['c_name', 'c_employeeN', 'c_website', 'c_street', 'c_state_zip_code',
        #                                   'c_country', 'p1c_name', 'p1c_role', 'p1c_phoneNumber', 'p1c_email',
        #                                   'p2c_name', 'p2c_role', 'p2c_phoneNumber', 'p2c_email', 'p3c_name',
        #                                   'p3c_role', 'p3c_phoneNumber', 'p3c_email', 'p1h_name', 'p1h_role',
        #                                   'p1h_phoneNumber', 'p1h_email', 'p2h_name', 'p2h_role', 'p2h_phoneNumber',
        #                                   'p2h_email', 'p3h_name', 'p3h_role', 'p3h_phoneNumber', 'p3h_email',
        #                                   'p1f_name', 'p1f_role', 'p1f_phoneNumber', 'p1f_email', 'p2f_name',
        #                                   'p2f_role', 'p2f_phoneNumber', 'p2f_email']
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item