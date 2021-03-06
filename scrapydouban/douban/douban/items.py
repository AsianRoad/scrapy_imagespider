# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()     #书名
    pub = scrapy.Field()       #出版信息
    date = scrapy.Field()      #日期
    tags = scrapy.Field()      #标签
    comment = scrapy.Field()   #评论
    pass
