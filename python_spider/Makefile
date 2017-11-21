#!/usr/bin/env bash
# 爬虫的name
name = jiuhua

run:
	scrapy crawl ${name}
json:
	scrapy crawl ${name} -o ./data/${name}.json
csv:
	scrapy crawl ${name} -o ./data/${name}.csv
dev:
	scrapy shell "http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=0&Astatus=1&type=1"