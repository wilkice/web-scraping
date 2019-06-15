# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        author_urls = response.xpath('//small/following-sibling::*[1]/@href').getall()
        for author_url in author_urls:
            yield response.follow(author_url, callback=self.parse_author)

        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        item = QuoteItem()
        item['name'] = response.xpath('//h3/text()').get().strip()
        item['born'] = response.xpath('//span[@class="author-born-date"]/text()').get()
        item['hometown'] = response.xpath('//span[@class="author-born-location"]/text()').get()
        yield item

