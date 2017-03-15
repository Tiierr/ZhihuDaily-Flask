from .base import Base
import urllib.request as http
import json

__all__ = ['Sections', 'Section']

class Sections(Base):
    def __init__(self):
        super(Sections, self).__init__()
        self.api = 'http://news-at.zhihu.com/api/4/sections'
        self._sections = self.data()
        self._length = self.length

    def getSections(self):
        return self.access(self.api)

    def data(self):
        return self.getSections()['data']

    @property
    def length(self):
        return len(self._sections)

    def section_at(self, i):
        if i > self._length:
            raise 'Index Error: index is not legal'
        return self._sections[i]


class Section(Base):
    def __init__(self, section):
        super(Section, self).__init__()
        self._section = section
        self.api = 'http://news-at.zhihu.com/api/4/section/{}'.format(self.sections_id)
        self._detail = self.detail()
        self._stories = self.stories()
        self._length = self.length

    def getDetails(self):
        return self.access(self.api)

    def detail(self):
        return self.getDetails()

    @property
    def length(self):
        return len(self._stories)


    @property
    def sections_id(self):
        try:
            return self._section['id']
        except:
            return ''

    @property
    def name(self):
        try:
            return self._section['name']
        except:
            return ''

    @property
    def description(self):
        try:
            return self._section['description']
        except:
            return ''

    @property
    def thumbnail(self):
        try:
            return self._detail['thumbnail']
        except:
            return ''

    def stories(self):
        return self._detail['stories']

    def story_at(self, i):
        if i > self._length:
            raise 'Index Error: index is not legal'
        return self._stories[i]
