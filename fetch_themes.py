#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.action import Theme, Themes, Story, NewsDetail, Content
from bs4 import BeautifulSoup
import requests
import time
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json
from time import sleep

eng = create_engine('sqlite:///data-dev.sqlite')

Base = declarative_base()

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    title = Column(String(128), index=True)
    url = Column(String(128))
    share_url = Column(String(128))
    image = Column(String(128))
    story_id = Column(String(8), unique=True)
    content = Column(Text)
    image_source = Column(String(128))
    css = Column(String(128))
    question_title = Column(String(128))
    avatar = Column(String(128))
    author = Column(String(48))
    bio = Column(String(128))
    original_url = Column(String(128))
    theme_id = Column(Integer)
    section_id = Column(Integer)


class Themess(Base):
    __tablename__ = 'themes'
    id = Column(Integer, primary_key=True, unique=True,  autoincrement=True)
    name = Column(String(48))
    description = Column(String(128))
    background = Column(String(128))
    image = Column(String(128))
    image_source = Column(String(128))
    themes_id = Column(Integer, unique=True)

Session = sessionmaker(bind=eng)
session = Session()


class FetchTheme(object):
    def addThemes(self, theme):
        themes_id = theme.themes_id
        session.add(Themess(name=theme.name, description=theme.description,
                        background=theme.background, image=theme.image,
                        image_source=theme.image_source,themes_id=theme.themes_id))
        session.commit()
        theme_id = [id[0] for id in session.query(Themess.id).filter(Themess.themes_id==themes_id)][0]
        return theme_id

    def addNews(self, theme, theme_id):
        print('*'*50)
        for i in range(theme.length):
            print('正在爬取第' + str(i + 1) + '条信息.')
            story = Story(theme.story_at(i))
            detail = NewsDetail(story.story_id)
            content = Content(detail.body)
            try:
                session.add(News(title=detail.title, url=detail.url,
                                share_url=detail.share_url, image=detail.image,
                                story_id=detail.detail_id, image_source=detail.image_source,
                                css=str(detail.css), question_title=str(content.question_title),
                                avatar=str(content.avatar), author=str(content.author),
                                bio=str(content.bio), content=str(content.content),
                                original_url=content.original_url,theme_id=theme_id))
                session.commit()
            except:
                pass

    def run(self):
        themes = Themes()
        for i in range(themes.length):
            theme = Theme(themes.theme_at(i))
            theme_id = self.addThemes(theme)
            self.addNews(theme, theme_id)

if __name__ == '__main__':
    FetchTheme().run()

  
