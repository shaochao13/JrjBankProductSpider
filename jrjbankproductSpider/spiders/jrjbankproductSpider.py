# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
import json


class JrjBankProductSpider(BaseSpider):
    allowed_domains = ["bank.jrj.com.cn"]
    start_urls = [u'http://bank.jrj.com.cn/action/bankproduct.jspa?page=1&order=SELL_END_DATE%20desc&bankid=0&cur=0&yield=0&sell=0&productname=&period=0&yieldtype=&holding=&atone=&beginDate=&endDate=&wf=1']
    name = 'jrjBankProductSpider'


    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        pageIndex = jsonresponse["page"]
        productsum = jsonresponse["pagesum"]
        products = jsonresponse["product"]

        for item in products:
            productID = item['productID']
            productName = item['productName']
            stopCond = item['stopCond']
            term = item['term']
            termType = item['termType']
            venture = item['venture']
            yield_Value = item['yield']
            yieldType = item['yieldType']
            yielddate = item['yielddate']
            yieldExplain = item['yieldExplain']
            addr = item["addr"]
            atoneBank = item['atoneBank']
            atoneCustormer = item['atoneCustormer']
            bankID = item['bankID']
            bankName = item['bankName']
            beginDate = item['beginDate']
            endDate = item['endDate']
            beginMoney = item['beginMoney']
            buyCond = item['buyCond']
            cur = item['cur']
            curncyType = item['curncyType']
            dp = item['dp']
            feature = item['feature']
            holding = item['holding']
            interestTerm = item['interestTerm']
            isQDII = item['isQDII']
            jf = item['jf']
            manageFee = item['manageFee']
            moneyUnit = item['moneyUnit']
            print(bankName)

        # 'http://bank.jrj.com.cn/action/bankproduct.jspa?page=1&order=SELL_END_DATE%20desc&bankid=0&cur=0&yield=0&sell=0&productname=&period=0&yieldtype=&holding=&atone=&beginDate=&endDate=&wf=1'


