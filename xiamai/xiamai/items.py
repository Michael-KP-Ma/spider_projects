# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiamaiItem(scrapy.Item):
    collection = table = 'products'
    id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    pub_time = scrapy.Field()
    discount = scrapy.Field()
    description = scrapy.Field()
    item_url = scrapy.Field()
