# -*- coding: utf-8 -*-
"""
need to specify: 
self.item_name: str
page: int
"""
import time
import re

import scrapy
from yhd.items import YhdItem


class YhdSpider(scrapy.Spider):
    name = 'yhd'

    def start_requests(self):
        self.item_name = 'iphone'
        page = 50
        for page in range(1, page + 1):
            time.sleep(2)
            # 每一页有2个 ajax 请求
            url_first = 'https://search.yhd.com/searchPage/c0-0/mbname-b/a-s1-v4-p{}-price-d0-f0b-m1-rt0-pid-mid0-color-size-k{}/'.format(
                page, self.item_name)
            url_second = 'https://search.yhd.com/searchPage/c0-0/mbname-b/a-s1-v4-p{}-price-d0-f0b-m1-rt0-pid-mid0-color-size-k{}/?isGetMoreProducts=1'.format(
                page, self.item_name)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3818.0 Safari/537.36 Edg/77.0.189.3',
                'Referer': 'https://search.yhd.com/c0-0/k{}/'.format(self.item_name),
            }
            yield scrapy.Request(url_first, callback=self.parse, headers=headers)
            yield scrapy.Request(url_second, callback=self.parse, headers=headers)

    def parse(self, response):
        content = response.text
        pattern = re.compile(
            r'<b>¥</b>(.*?)\\n\\t</em>.*?title=\\"(.*?)\\"', re.S)
        for good in re.findall(pattern, content):
            item = YhdItem()
            item['name'] = self.item_name
            item['price'] = good[0]
            item['info'] = good[1]
            yield item
