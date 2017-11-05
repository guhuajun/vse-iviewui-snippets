# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class SnippetspiderSpider(scrapy.Spider):
    name = 'SnippetSpider'
    allowed_domains = ['iviewui.com']
    start_urls = ['https://www.iviewui.com/docs/guide/install']

    def start_requests(self):
        # https://blog.scrapinghub.com/2015/03/02/handling-javascript-in-scrapy-with-splash/
        for url in self.start_urls:
            yield SplashRequest(
                url, self.parse_page, endpoint='render.html', args={
                    'wait': 10
                })

    def parse_component(self, response):
        '''get example'''
        examples = response.xpath('//article/div[@class="example]')
        print(examples)

    def parse_page(self, response):
        '''get component name'''
        menus = response.xpath('//ul/li[@class="ivu-select-item"]')
        for menu in menus:
            text = str(menu.xpath('text()').extract())
            component = ''.join(text.split(' ')[0][2:]).lower()
            yield SplashRequest(
                'https://www.iviewui.com/components/{0}'.format(component),
                callback=self.parse_component, endpoint='render.html', args={
                    'wait': 10
                })
