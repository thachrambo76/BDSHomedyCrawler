# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class W1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
        title = scrapy.Field()
        fee = scrapy.Field()
        location = scrapy.Field()
        author = scrapy.Field()
