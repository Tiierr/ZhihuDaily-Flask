
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from app.action import Sections, Section, Story, NewsDetail, Content
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


class Sectionss(Base):
    __tablename__ = 'sections'
    id = Column(Integer, primary_key=True, unique=True, index=True)
    name = Column(String(48))
    description = Column(String(128))
    thumbnail = Column(String(128))
    sections_id = Column(Integer, unique=True)

Session = sessionmaker(bind=eng)
session = Session()


class FetchSection(object):
    def addSections(self, section):
        session.add(Sectionss(name=section.name, description=section.description,
                        thumbnail=section.thumbnail, sections_id=section.sections_id))
        session.commit()
        section_id = [id[0] for id in session.query(Sectionss.id).filter(Sectionss.sections_id==section.sections_id)][0]
        return section_id

    def addNews(self, section, section_id):
        print('*'*50)
        for i in range(section.length):
            print('正在爬取第' + str(i + 1) + '条信息.')
            story = Story(section.story_at(i))
            detail = NewsDetail(story.story_id)
            content = Content(detail.body)
            try:
                session.add(News(title=detail.title, url=detail.url,
                                share_url=detail.share_url, image=detail.image,
                                story_id=detail.detail_id, image_source=detail.image_source,
                                css=str(detail.css), question_title=str(content.question_title),
                                avatar=str(content.avatar), author=str(content.author),
                                bio=str(content.bio), content=str(content.content),
                                original_url=content.original_url,section_id=section_id))
                session.commit()
            except:
                pass

    def run(self):
        sections = Sections()
        for i in range(sections.length):
            section = Section(sections.section_at(i))
            section_id = self.addSections(section)
            self.addNews(section, section_id)

if __name__ == '__main__':
    FetchSection().run()
