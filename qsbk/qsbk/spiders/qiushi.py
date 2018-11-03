# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList


class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_url = 'https://www.qiushibaike.com'

    def parse(self, response):
        duanzi_div = response.xpath('//div[@id="content-left"]/div')
        for duanzi in duanzi_div:
            author = duanzi.xpath('.//h2/text()').get().strip()
            content = duanzi.xpath('.//div[@class="content"]//text()').getall()
            content = ''.join(content).strip()
            item = QsbkItem(author=author, content=content)
            yield item

        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()
        if next_url:
            yield scrapy.Request(self.base_url+next_url, self.parse)
