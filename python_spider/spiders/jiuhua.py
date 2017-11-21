# -*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(".")
import scrapy
import re
import json
import time
from python_spider.items import PythonSpiderItem2
from scrapy.http import Request
from python_spider.data import data

class TestUrl(scrapy.Spider):
    name = "jiuhua"
    allowed_domains = ["weixin.jiuhuar.com"]
    start_urls = data.URLLIST
    # i = 0
    def parse(self, response):
        # item = []
        item = PythonSpiderItem2()
        # body = response.body.decode('unicode_escape')
        body_dic = json.loads(response.body_as_unicode())
        if len(body_dic["data"]) != 0:
            for i in range(len(body_dic["data"])):
                oid = body_dic["data"][i]["oid"]
                link = "https://weixin.jiuhuar.com/api/bar/" + oid
                yield Request(link,callback=self.parse2)

                url = response.url
                pattern = '&p=([0-9].*?)'
                match = re.findall(pattern,url)
                page = '&p='+str(int(match[0])+1)
                link2 = re.sub(pattern,page,url)

                yield Request(link2,callback=self.parse)


    def parse2(self, response):
        # item = []
        item = PythonSpiderItem2()
        # body = response.body.decode('unicode_escape')
        body_dic = json.loads(response.body_as_unicode())
        item['name'] = body_dic["data"]["bar"]["name"]
        item['address'] = body_dic["data"]["bar"]["address"]
        item['tel'] = body_dic["data"]["bar"]["tel"]
        yield item

