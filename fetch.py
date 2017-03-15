#!/usr/bin/env python
# -*- coding: utf-8 -*-
__all__ = ['Fetch']

from app.action import Datetime, News, Content, Daily, Details
from sqlalchemy import create_engine, Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from celery import Celery
from celery.schedules import crontab

from bs4 import BeautifulSoup
from datetime import datetime,timedelta
from time import sleep

import json
import requests
import time

app = Celery('fetch',backend='amqp://guest@localhost//', broker='amqp://guest@localhost//')

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'perminute': {
            'task': 'fetch.run',
            'schedule': crontab(minute=0, hour='*/2')
        }
    }
)

eng = create_engine('sqlite:///data-dev.sqlite')

Base = declarative_base()

class Dates(Base):
    __tablename__ = 'dates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    dates = Column(String(8), unique=True, index=True)

class Stories(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(128), index=True)
    url = Column(String(128), unique=True)
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
    date_id = Column(Integer)

Session = sessionmaker(bind=eng)
session = Session()

class Fetch(object):
    def addDates(self, date):
        news = News().getBeforeNews(date)
        daily = Daily(news)
        try:
            date_id = [id[0] for id in session.query(Dates.id).filter(Dates.dates==daily.date)][0]
        except:
            date_id = None
        if date_id is None:
            session.add(Dates(dates=daily.date))
            session.commit()
            date_id = [id[0] for id in session.query(Dates.id).filter(Dates.dates==daily.date)][0]
        return daily, date_id


    def addNews(self, date, daily, date_id):
        print('*'*50)
        for i in range(daily.length)[::-1]:
            detail = Details(daily.news_at(i))
            content = Content(detail.body)
            try:
                story_id = [id[0] for id in session.query(Stories.id).filter(Stories.story_id==detail.id)][0]
            except:
                story_id = None

            if story_id is None:
                print('正在爬取' + date + '的第' + str(daily.length - i) + '条信息.')
                session.add(Stories(title=detail.title, url=detail.url,
                                share_url=detail.share_url, image=detail.image,
                                story_id=detail.id, image_source=detail.image_source,
                                css=str(detail.css), question_title=str(content.question_title),
                                avatar=str(content.avatar), author=str(content.author),
                                bio=str(content.bio), content=str(content.content),
                                original_url=content.original_url,date_id=date_id))
                session.commit()

    def fetch(self):
        for i in range(2)[::-1]:
            if i % 5 == 0:
                sleep(5)
            date = Datetime()
            daily, date_id = self.addDates(date.before(i))
            if date_id is not None:
                self.addNews(date.yesterday, daily, date_id)
@app.task
def run():
    Fetch().fetch()

if __name__ == '__main__':
    run.delay()
