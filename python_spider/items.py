# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class PythonSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    channel = scrapy.Field() #渠道
    title = scrapy.Field()   #标题
    name = scrapy.Field()    #发起人名字
    area = scrapy.Field()    #地区
    time = scrapy.Field()    #发起时间
    type = scrapy.Field()    #类别
    purpose = scrapy.Field() #目的
    target = scrapy.Field()  #目标金额
    completed = scrapy.Field() #完成进度
    hasRaised = scrapy.Field() #已筹金额
    support = scrapy.Field() #支持人数
    link = scrapy.Field()   #项目链接
    # desc = scrapy.Field()

    # pass

class PythonSpiderItem2(scrapy.Item):
    # oid = scrapy.Field() #oid
    tel = scrapy.Field()
    address = scrapy.Field()
    name = scrapy.Field()

# class PythonSpiderItem3(scrapy.Item):