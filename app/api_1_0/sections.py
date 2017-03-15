from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import Sections, News
from . import api
from .errors import forbidden

@api.route('/sections/')
def get_sections():
    sections = Sections.query.order_by(Sections.id)
    return jsonify({
        'name': '主题',
        'sections': [section.to_json() for section in sections]
    })

@api.route('/section/<int:id>')
def get_section(id):
    section = Sections.query.filter_by(id=id).first_or_404()
    _news = section.stories.order_by(News.id)
    return jsonify({
        'section': section.name,
        'description': section.description,
        'news': [news.to_json_simple() for news in _news]
    })
