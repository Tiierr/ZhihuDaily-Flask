#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import Base
import urllib.request as http
import json

__all__ = ['Themes', 'Theme', 'Story', 'NewsDetail']

class Themes(Base):
    def __init__(self):
        super(Themes, self).__init__()
        self.api = 'http://news-at.zhihu.com/api/4/themes'
        self._themes = self.others()
        self._length = self.length

    def getThemes(self):
        return self.access(self.api)

    def others(self):
        return self.getThemes()['others']

    @property
    def length(self):
        return len(self._themes)

    def theme_at(self, i):
        if i > self._length:
            raise 'Index Error: index is not legal'
        return self._themes[i]


class Theme(Base):
    def __init__(self, theme):
        super(Theme, self).__init__()
        self._theme = theme
        self.api = 'http://news-at.zhihu.com/api/4/theme/{}'.format(self.themes_id)
        self._detail = self.detail()
        self._stories = self.stories
        self._length = self.length


    def getDetails(self):
        return self.access(self.api)

    def detail(self):
        return self.getDetails()

    @property
    def length(self):
        return len(self._stories)

    @property
    def themes_id(self):
        return self._theme['id']

    @property
    def name(self):
        return self._theme['name']

    @property
    def description(self):
        return self._theme['description']

    @property
    def background(self):
        return self._detail['background']

    @property
    def image(self):
        return self._detail['image']

    @property
    def image_source(self):
        return self._detail['image_source']

    @property
    def stories(self):
        return self._detail['stories']

    def story_at(self, i):
        if i > self._length:
            raise 'Index Error: index is not legal'
        return self._stories[i]

class Story(object):
    def __init__(self, story):
        self._story = story

    @property
    def story_id(self):
        return self._story['id']

    @property
    def title(self):
        return self._story['title']

    @property
    def image(self):
        try:
            return self._story['image']
        except:
            return ''

class NewsDetail(Base):
    def __init__(self, id):
        super(NewsDetail, self).__init__()
        self._story_id = id
        self._detail = self.detail()

    def getNewsDetails(self, _id):
        return self.access(self.apiID.format(_id))

    def detail(self):
        return self.getNewsDetails(self._story_id)

    @property
    def title(self):
        return self._detail['title']

    @property
    def detail_id(self):
        return self._detail['id']

    @property
    def css(self):
        try:
            return self._detail['css']
        except:
            return ''

    @property
    def image_source(self):
        try:
            return self._detail['image_source']
        except:
            return ''

    @property
    def body(self):
        try:
            return self._detail['body']
        except:
            return ''

    @property
    def image(self):
        try:
            return self._detail['image']
        except:
            return ''

    @property
    def share_url(self):
        return self._detail['share_url']

    @property
    def url(self):
        return self.apiID.format(self._story_id)
