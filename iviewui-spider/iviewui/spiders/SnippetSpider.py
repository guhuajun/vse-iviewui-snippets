# -*- coding: utf-8 -*-
import scrapy


class SnippetspiderSpider(scrapy.Spider):
    name = 'SnippetSpider'
    allowed_domains = ['iviewui.com']
    start_urls = ['https://www.iviewui.com/docs/guide/install']

    def parse(self, response):
        print(response.body)
