# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeizituItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	date = scrapy.Field()
	title = scrapy.Field()
	image_urls = scrapy.Field()
	imags = scrapy.Field()
	image_paths = scrapy.Field()



