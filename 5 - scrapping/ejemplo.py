#!/usr/bin/python
# -*- coding: utf-8 -*-

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from scrapy.http import Request


class Rastreador(BaseSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = [
    'http://www.example.com/1.html',
    'http://www.example.com/2.html',
    'http://www.example.com/3.html',
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        for h3 in hxs.select('//h3').extract():
            yield MyItem(title=h3)
            for url in hxs.select('//a/@href').extract():
                yield Request(url, callback=self.parse)

r1=Rastreador()
