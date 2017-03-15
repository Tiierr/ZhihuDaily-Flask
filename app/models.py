from . import db
from flask import url_for, current_app
from jieba.analyse import ChineseAnalyzer

class Dates(db.Model):
    __tablename__ = 'dates'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    dates = db.Column(db.String(8), unique=True, index=True)
    stories = db.relationship('Stories', backref='date', lazy='dynamic')

class Stories(db.Model):
    __tablename__ = 'stories'
    __searchable__ = ['title', 'question_title']
    __analyzer__ = ChineseAnalyzer()
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    title = db.Column(db.String(128), index=True)
    url = db.Column(db.String(128))
    share_url = db.Column(db.String(128))
    image = db.Column(db.String(128))
    story_id = db.Column(db.String(8), unique=True)
    content = db.Column(db.Text)
    image_source = db.Column(db.String(128))
    css = db.Column(db.String(128))
    question_title = db.Column(db.String(128))
    avatar = db.Column(db.String(128))
    author = db.Column(db.String(48))
    bio = db.Column(db.String(128))
    original_url = db.Column(db.String(128))
    date_id = db.Column(db.Integer, db.ForeignKey('dates.id'))

    def to_json(self):
        json_story = {
            'id' : self.id,
            'title': self.title,
            'share_url': self.share_url,
            'image': self.image,
            'story_id': self.story_id,
            'content': self.content,
            'image_source': self.image_source,
            'question_title': self.question_title,
            'avatar': self.avatar,
            'author': self.author,
            'bio': self.bio,
            'original_url': self.original_url,
            'alt': url_for('main.story', id=self.id, _external=True),
            'url': url_for('api.get_story', id=self.id, _external=True),
        }
        return json_story

    def to_json_simple(self):
        json_story = {
            'title': self.title,
            'id' : self.id,
            'share_url': self.share_url,
            'image': self.image,
            'story_id': self.story_id,
            'alt': url_for('main.story', id=self.id, _external=True),
            'url': url_for('api.get_story', id=self.id, _external=True),
        }
        return json_story

    def __repr__(self):
        return '<Stories %r>' % self.name

class News(db.Model):
    __tablename__ = 'news'
    __searchable__ = ['title', 'question_title']
    __analyzer__ = ChineseAnalyzer()
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    title = db.Column(db.String(128), index=True)
    url = db.Column(db.String(128))
    share_url = db.Column(db.String(128))
    image = db.Column(db.String(128))
    story_id = db.Column(db.String(8))
    content = db.Column(db.Text)
    image_source = db.Column(db.String(128))
    css = db.Column(db.String(128))
    question_title = db.Column(db.String(128))
    avatar = db.Column(db.String(128))
    author = db.Column(db.String(48))
    bio = db.Column(db.String(128))
    original_url = db.Column(db.String(128))
    theme_id = db.Column(db.Integer, db.ForeignKey('themes.id'))
    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'))

    def __repr__(self):
        return '<News %r>' % self.name


    def to_json(self):
        json_news = {
            'id' : self.id,
            'title': self.title,
            'share_url': self.share_url,
            'image': self.image,
            'story_id': self.story_id,
            'content': self.content,
            'image_source': self.image_source,
            'question_title': self.question_title,
            'avatar': self.avatar,
            'author': self.author,
            'bio': self.bio,
            'original_url': self.original_url,
            'alt': url_for('main.new', id=self.id, _external=True),
            'url': url_for('api.get_news', id=self.id, _external=True),
        }
        return json_news

    def to_json_simple(self):
        json_news = {
            'title': self.title,
            'id' : self.id,
            'share_url': self.share_url,
            'image': self.image,
            'news_id': self.story_id,
            'alt': url_for('main.new', id=self.id, _external=True),
            'url': url_for('api.get_news', id=self.id, _external=True),
        }
        return json_news

class Themes(db.Model):
    __tablename__ = 'themes'
    __searchable__ = ['name']
    __analyzer__ = ChineseAnalyzer()
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    name = db.Column(db.String(48))
    description = db.Column(db.String(128))
    background = db.Column(db.String(128))
    image = db.Column(db.String(128))
    image_source = db.Column(db.String(128))
    themes_id = db.Column(db.Integer, unique=True)
    stories = db.relationship('News', backref='theme', lazy='dynamic')

    def to_json(self):
        json_theme = {
            'name': self.name,
            'id' : self.id,
            'description': self.description,
            'image': self.image,
            'alt': url_for('main.theme', id=self.id, _external=True),
            'url': url_for('api.get_theme', id=self.id, _external=True),
        }

        return json_theme

    def __repr__(self):
        return '<Themes %r>' % self.name

class Sections(db.Model):
    __tablename__ = 'sections'
    __searchable__ = ['name']
    __analyzer__ = ChineseAnalyzer()
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    name = db.Column(db.String(48))
    description = db.Column(db.String(128))
    thumbnail = db.Column(db.String(128))
    sections_id = db.Column(db.Integer, unique=True)
    stories = db.relationship('News', backref='section', lazy='dynamic')

    def to_json(self):
        json_section = {
            'name': self.name,
            'id' : self.id,
            'description': self.description,
            'thumbnail': self.thumbnail,
            'alt': url_for('main.section', id=self.id, _external=True),
            'url': url_for('api.get_section', id=self.id, _external=True),
        }

        return json_section

    def __repr__(self):
        return '<Sections %r>' % self.name
