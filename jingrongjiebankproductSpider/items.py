# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingRongJiebankproductItem(scrapy.Item):
    productID = scrapy.Field()
    productName = scrapy.Field()
    #银行提前终止条件
    # stopCond = scrapy.Field()
    #委托管理期限
    term = scrapy.Field()
    #委托管理期限的单位，1-月，2-天
    termType = scrapy.Field()
    #投资风险说明
    venture = scrapy.Field()
    #预期年收益率
    yield_Value = scrapy.Field()
    #收益类型
    # yieldType = scrapy.Field()
    #收益率说明
    # yieldExplain = scrapy.Field()
    #发售地区
    addr = scrapy.Field()
    #银行名称
    bankName = scrapy.Field()
    #发行起始日期
    beginDate = scrapy.Field()
    #发行终止日期
    endDate = scrapy.Field()
    #委托币种起始金额
    beginMoney = scrapy.Field()
    #申购条件说明
    # buyCond = scrapy.Field()
    #币种
    cur = scrapy.Field()
    #产品特色
    feature = scrapy.Field()
    #是否保本
    # holding = scrapy.Field()
