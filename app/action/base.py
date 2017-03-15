#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request as http
import json
import re #正则表达式

__all__ = ['Base']

class Base(object):
    def __init__(self):
        self.apiLatest='http://news.at.zhihu.com/api/1.2/news/latest/'
        self.apiBefore='http://news.at.zhihu.com/api/1.2/news/before/{}'
        self.apiID='http://news-at.zhihu.com/api/1.2/news/{}'

        #知乎日报禁止了爬虫,因此要模拟浏览器访问
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }

    def access(self,url):
        self.req=http.Request(url,headers=self.headers)
        self.fp=http.urlopen(self.req)
        self.mybytes=self.fp.read()
        self.mystr=self.mybytes.decode("utf8")
        self.fp.close()
        return json.loads(self.mystr)
