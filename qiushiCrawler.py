# -*- coding:utf-8 -*-

#爬取糗事百科段子

import urllib
import urllib2
import re

# page = 1
def scanQiushi(page):
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    try:
        request = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        #print content
        pattern = re.compile('<h2>(.*?)</h2>.*?<div class="content">\s+<span>(.*?)</span>\s+</div>',re.S)
        items = re.findall(pattern,content)
        #print items
        print '第',page,'页内容:\n'
        for item in items:
            print '作者:',item[0],'\n','内容:',re.sub(r'<br[ ]?/?>', '\n', item[1]),'\n'
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason


for i in range(5):
    scanQiushi(i+1)