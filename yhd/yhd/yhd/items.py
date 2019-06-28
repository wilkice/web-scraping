# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YhdItem(scrapy.Item):
    # define the fields for your item here like:
    table = collection = 'products'
    name = scrapy.Field()
    price = scrapy.Field()
    info = scrapy.Field()
