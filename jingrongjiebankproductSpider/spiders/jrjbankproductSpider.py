# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
import json
from scrapy.http import Request
from jingrongjiebankproductSpider.items import JingRongJiebankproductItem
import MySQLdb
import redis


class JingRongJieBankProductSpider(BaseSpider):
    def __init__(self):
        self.conn = MySQLdb.connect(host="10.1.1.32", user="dev", passwd="dev", db="hj_wealth", charset="utf8")
        self.cursor = self.conn.cursor()
        self.r = redis.StrictRedis(host='10.1.1.33', port=6379, db=13)


    allowed_domains = ["bank.jrj.com.cn"]
    start_urls = [u'http://bank.jrj.com.cn/action/bankproduct.jspa?page=1&order=SELL_END_DATE%20desc&bankid=0&cur=0&yield=0&sell=0&productname=&period=0&yieldtype=&holding=&atone=&beginDate=&endDate=&wf=1']
    name = 'jrjBankProductSpider'

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        pageIndex = jsonresponse["page"]
        pageIndex = int(pageIndex) + 1
        productsum = jsonresponse["pagesum"]
        products = jsonresponse["product"]
        items = []
        if len(products) > 0:
            for info in products:
                yield self.parse_two(info)

            url = u'http://bank.jrj.com.cn/action/bankproduct.jspa?page=%s&order=SELL_END_DATE desc&bankid=0&cur=0&yield=0&sell=0&productname=&period=0&yieldtype=&holding=&atone=&beginDate=&endDate=&wf=1' % pageIndex
            yield Request(url=url, callback=self.parse)



    def parse_two(self, info):
        item = JingRongJiebankproductItem()

        item['productID'] = info['productID']

        # productName = info['productName']
        #银行提前终止条件
        # stopCond = info['stopCond']

        #委托管理期限
        term = info['term']
        #委托管理期限的单位，1-月，2-天
        termType = info['termType']
        try:
            item['term'] = int(term)
            if termType == 2:
                item['termType'] = 0
            else:
                item['termType'] = termType
        except:
            item['term'] = -1
            item['termType'] = -1

        #预期年收益率
        # yield_Value = info['yield']
        # try:
        #     item['yield_Value'] = float(yield_Value) / 100.0
        # except:
        #     item['yield_Value'] = -1

        #收益类型
        # item['yieldType'] = info['yieldType']
        #收益率说明
        # yieldExplain = info['yieldExplain']
        #发售地区
        addrs = info["addr"].strip().split(' ')
        if len(addrs) > 1:
            addrs = ','.join(addrs)
            item['addr'] = addrs
        else:
            item['addr'] = info["addr"]
        #银行ID
        # bankID = info['bankID']
        #银行名称
        item['bankName'] = info['bankName']
        #发行起始日期
        beginDate = info['beginDate']
        if len(beginDate) > 0:
            tmp = (beginDate[0]).split('-')
            if len(tmp) == 3:
                item["beginDate"] = "'%s'" % beginDate
            else:
                item["beginDate"] = "NULL"
        else:
            item["beginDate"] = "NULL"

        #发行终止日期
        endDate = info['endDate']
        if len(endDate) > 0:
            tmp = (endDate[0]).split('-')
            if len(tmp) == 3:
                item["endDate"] = "'%s'" % endDate
            else:
                item["endDate"] = "NULL"
        else:
            item["endDate"] = "NULL"

        #委托币种起始金额
        item['beginMoney'] = info['beginMoney']
        #申购条件说明
        # buyCond = info['buyCond']
        #币种
        item['cur'] = info['cur']
        #产品特色
        item['feature'] = info['feature']
        #投资风险说明
        item['venture'] = info['venture']
        #是否保本
        # holding = info['holding']
        return item


