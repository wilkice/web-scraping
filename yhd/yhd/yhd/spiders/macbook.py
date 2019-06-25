# -*- coding: utf-8 -*-
import time
from urllib.parse import urlencode
import re

import scrapy
from yhd.items import YhdItem


class MacbookSpider(scrapy.Spider):
    name = 'macbook'

    def start_requests(self):
        for page in range(1, 17):
            time.sleep(2)
            base_url = 'http://search.yhd.com/searchPage/c0-0/mbnameApple-b/a-s1-v4-p{}-price-d0-f0b-m1-rt0-pid-mid0-color-size-kmacbook/?'.format(
                page)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3818.0 Safari/537.36 Edg/77.0.189.3',
                'Referer': 'https://search.yhd.com/c0-0/kmacbook/',
            }
            params = {
                'isLargeImg': 0,
                'fashionCateType': 2,
                'onlySearchKeyword': 1,
                '_': int(time.time() * 1000),
            }
            url = base_url + urlencode(params)
            yield scrapy.Request(url, callback=self.parse, headers=headers)

            params_second = {
                "isGetMoreProducts": "1",
                "moreProductsDefaultTemplate": "0",
                "isLargeImg": "0",
                "moreProductsFashionCateType": "2",
                "nextAdIndex": "0",
                "nextImageAdIndex": "0",
                "adProductIdListStr": "",
                "fashionCateType": "2",
                "firstPgAdSize": "0",
                "needMispellKw": "",
                "onlySearchKeyword": "1",
                "_": int(time.time() * 1000),
            }
            url_second = base_url + urlencode(params_second)
            yield scrapy.Request(url_second, callback=self.parse, headers=headers)

    def parse(self, response):
        content = response.text
        pattern = re.compile(
            r'<b>¥</b>(.*?)\\n\\t</em>.*?title=\\"(.*?)\\"', re.S)
        for good in re.findall(pattern, content):
            item = YhdItem()
            item['name'] = 'Macbook'
            item['price'] = good[0]
            item['info'] = good[1]
            yield item
