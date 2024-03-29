# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class JobsSpiderPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('localhost',27017)
        scrapy_db = client['scrapy_db']
        self.coll =scrapy_db['job_scrapy']
    def process_item(self, item, spider):
        self.coll.insert_one(item)
        return item
