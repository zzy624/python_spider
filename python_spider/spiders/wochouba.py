# -*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append(".")
import scrapy
import re
import json
import time
from python_spider.items import PythonSpiderItem
from scrapy.http import Request

class TestUrl(scrapy.Spider):
    name = "wcb"
    allowed_domains = ["wx.wochou8.com"]
    start_urls = ["http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=1&Astatus=0&type=1",
                  "http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=1&Astatus=1&type=1",
                  "http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=1&Astatus=2&type=1",
                  "http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=1&Astatus=3&type=1",
                  "http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=1&Astatus=4&type=1",
                  "http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=1&Astatus=5&type=1",
                  "http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=1&Astatus=6&type=1",
                  "http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=1&Astatus=7&type=1",
                  "http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=1&Astatus=8&type=1"
                  ]
    i = 0
    def parse(self, response):
        # item = []
        item = PythonSpiderItem()
        # body = response.body.decode('unicode_escape')
        # print body
        body_dic = json.loads(response.body_as_unicode())
        # print sites["can_load_more"]
        if isinstance(body_dic,dict):
            # if body_dic["can_load_more"] == 1:
                # print body_dic["0"]
                try:
            #     body = body.split(',"can_load_more"')[1]
            #     body_dic = eval(body)
            #     print body
            #     except TypeError,e:
                    with open('data.txt','ab') as f:
                        f.write(response.url + '\n')
            #     raise e
                    list = ['0','1','2','3','4']
                    for i in list:
                        item['channel'] = body_dic[i][1]
                        item['title'] = body_dic[i][2]
                        item['name'] = body_dic[i][3]
                        item['area'] = body_dic[i][4]
                        item['time'] = body_dic[i][5]
                        item['purpose'] = body_dic[i][6]
                        item['type'] = body_dic[i][7]
                        item['target'] = body_dic[i][8]
                        item['hasRaised'] = body_dic[i][9]
                        item['completed'] = body_dic[i][10]
                        item['support'] = body_dic[i][11]
                        item['link'] = body_dic[i][12]
                        yield item

                        url = response.url
                        pattern = 'Apage=([0-9].*?)&'
                        match = re.findall(pattern,url)
                        page = 'Apage='+str(int(match[0])+1) + "&"
                        link = re.sub(pattern,page,url)

                        yield Request(link,callback=self.parse)

                except TypeError,e:
                    with open('error.txt','ab') as f:
                        f.write(str(body_dic))
                    print e
                    time.sleep(1)
                    i = self.i + 1
                    yield Request(self.start_urls[i],callback=self.parse)

