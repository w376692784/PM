# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()
    date = scrapy.Field()
    quality_level = scrapy.Field()
    AQI = scrapy.Field()
    AQI_level = scrapy.Field()
    PM2_5 = scrapy.Field()
    PM10 = scrapy.Field()
    So2 = scrapy.Field()
    No2 = scrapy.Field()
    Co = scrapy.Field()
    O3 = scrapy.Field()
