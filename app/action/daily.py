#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['Daily']

class Daily(object):
    def __init__(self, news):
        self._news = news
        self._length = self.length

    @property
    def date(self):
        return self._news['date']

    @property
    def display_date(self):
        return self._news['display_date']

    @property
    def length(self):
        return len(self._news['news'])

    def news_at(self, i):
        if i > self._length:
            raise 'Index Error: index is not legal'
        return self.allNews[i]

    @property
    def allNews(self):
        return self._news['news']
