# -*-coding:utf-8-*-
# 调试脚本

import re
if __name__ == '__main__':
    url =''',""http://wx.wochou8.com/m/?ctl=gucun&act=ajax_get_gucun_array&Apage=12&Astatus=1&type=1"","",'''
    print url
    pattern = re.compile(r',(\"\")')
    match = pattern.match(url)
    print match
    # page = 'Apage'+str(int(match[0])+1) + "&"
    result = re.sub(pattern,",\"",url)
    print result