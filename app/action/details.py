#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .base import Base
import urllib.request as http
import json

__all__ = ['Details']

class Details(Base):
    def __init__(self, news):
        super(Details, self).__init__()
        self._news = news
        self._detail = self.detail()

    def getNewsDetails(self, _id):
        return self.access(self.apiID.format(_id))

    @property
    def share_url(self):
        return self._news['share_url']

    @property
    def title(self):
        return self._news['title']

    @property
    def url(self):
        return self._news['url']

    @property
    def id(self):
        return self._news['id']

    @property
    def image(self):
        return self._news['image']

    def detail(self):
        return self.getNewsDetails(self.id)

    @property
    def css(self):
        return self._detail['css']

    @property
    def image_source(self):
        return self._detail['image_source']

    @property
    def body(self):
        return self._detail['body']
