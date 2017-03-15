# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

__all__ = ['Content']

class Content(object):
    def __init__(self, content):
        self._content = content

    @property
    def soup(self):
        return BeautifulSoup(self._content, 'lxml')

    @property
    def question_title(self):
        try:
            return self.soup.findAll("h2", {"class":"question-title"})[-1].get_text().strip()
        except:
            return " "

    @property
    def avatar(self):
        try:
            return self.soup.findAll("img", {"class":"avatar"})[-1]['src']
        except:
            return " "

    @property
    def author(self):
        try:
            return self.soup.findAll("span", {"class":"author"})[-1].get_text()
        except:
            return " "

    @property
    def bio(self):
        try:
            return self.soup.findAll("span", {"class":"bio"})[-1].get_text()
        except:
            return " "

    @property
    def content(self):
        try:
            return self._content
        except:
            return " "

    @property
    def original_url(self):
        try:
            return self.soup.findAll("a")[-1]['href']
        except:
            return " "
