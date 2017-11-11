# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup

from iviewui.items import Snippet

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

        component = response.xpath('//article/h1/text()').extract()[0].lower()
        examples = response.xpath('//article/div[@class="example ivu-row"]')
        for example in examples:
            snippet = Snippet()
            example_id = example.xpath('@id').extract()[0]
            example_name = example.xpath('@id').extract()[0].lower()
            example_name = example_name.replace(' ', '-')

            code = example.xpath('//code/child::*').extract()
            code = '\n'.join(code)
            code = BeautifulSoup(code, 'lxml').text
            code = BeautifulSoup(code, 'lxml').prettify()
            code = code.split('\n')
            code = list(filter(
                lambda x: x not in ['<html>', '</html>', ' <body>', ' </body>'], code))
            code = [x[2:] for x in code]

            snippet['prefix'] = 'iviewui-{0}-{1}'.format(component, example_name)
            snippet['description'] = example_id
            snippet['body'] = code

            yield snippet

    def parse_page(self, response):
        '''get component name'''
        menus = response.xpath('//ul/li[@class="ivu-select-item"]')
        for menu in menus:
            text = str(menu.xpath('text()').extract())
            component = ''.join(text.split(' ')[0][2:]).lower()
            yield SplashRequest(
                'https://www.iviewui.com/components/{0}-en'.format(component),
                callback=self.parse_component, endpoint='render.html', args={
                    'wait': 10
                })
            break
