# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QianchengSpiderSpider(CrawlSpider):
    name = 'qiancheng_spider'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/080300,000000,0000,00,9,99,python,2,1.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://jobs.51job.com/ningbo.*/\d+\.html.*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['job_name'] = response.xpath('//div[@class="cn"]/h1/@title').get()
        item['job_price'] = response.xpath('//div[@class="cn"]/strong/text()').get()
        item['job_area'] = response.xpath('//div[@class="cn"]/p/@title').get()
        item['job_url'] = response.url
        item['flag'] = "前程无忧"
        print(item)
        return item
