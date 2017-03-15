#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import Base
import urllib.request as http
import json

__all__ = ['News']

class News(Base):
    def __init__(self):
        super(News, self).__init__()

    def getLatestNews(self):
        return self.access(self.apiLatest)

    def getBeforeNews(self,date):
        return self.access(self.apiBefore.format(date))
