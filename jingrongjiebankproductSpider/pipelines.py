# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import redis

class JingRongJiebankproductspiderPipeline(object):

    def __init__(self):
        self.conn = MySQLdb.connect(host="10.1.1.32", user="dev", passwd="dev", db="hj_wealth", charset="utf8")
        self.cursor = self.conn.cursor()
        self.r = redis.StrictRedis(host='10.1.1.33', port=6379, db=13)

    def process_item(self, item, spider):
        print('----------------------------------')

        sql = """insert into tbl_bank_financial_product_jrj(
                            manage_period,
                            manage_period_unit,
                            sale_cities,
                            org_name,
                            sale_start_date,
                            sale_stop_date,
                            delegate_amount,
                            currency,
                            product_feature,
                            data_source,
                            data_source_tag,
                            create_date,
                            last_update_date) VALUES(
                            '%s',
                            '%s',
                            '%s',
                            '%s',
                             %s,
                             %s,
                            '%s',
                            '%s',
                            '%s',
                            'jrj',
                            '%s',
                            now(),
                            now()
                            );""" % (
                            item['term'],
                            item['termType'],
                            item['addr'],
                            item['bankName'],
                            item['beginDate'],
                            item['endDate'],
                            item['beginMoney'],
                            item['cur'],
                            item['feature'],
                            item['productID']
                        )

        if not self.r.sismember("jrjproductIDs", item['productID']):
            try:
                n = self.cursor.execute(sql)
                self.conn.commit()
                if n > 0:
                    self.r.sadd("jrjproductIDs", item['productID'])
            except MySQLdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])


        print('----------------------------------')

        return item
