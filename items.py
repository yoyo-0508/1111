# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:

    user_id = scrapy.Field()
    screen_name = scrapy.Field()
    text = scrapy.Field()
    
    topics = scrapy.Field()
    reposts_count = scrapy.Field()
    comments_count = scrapy.Field()
    attitudes_count = scrapy.Field()
    created_at = scrapy.Field()
    
    pics = scrapy.Field()

    ip = scrapy.Field()

