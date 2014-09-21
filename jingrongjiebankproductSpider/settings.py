# -*- coding: utf-8 -*-

# Scrapy settings for jingrongjiebankproductSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'jingrongjiebankproductSpider'

SPIDER_MODULES = ['jingrongjiebankproductSpider.spiders']
NEWSPIDER_MODULE = 'jingrongjiebankproductSpider.spiders'
ITEM_PIPELINES = ['jingrongjiebankproductSpider.pipelines.JingRongJiebankproductspiderPipeline']
LOG_LEVEL = 'INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jingrongjiebankproductSpider (+http://www.yourdomain.com)'
