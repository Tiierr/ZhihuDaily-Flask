from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import Themes, News
from . import api
from .errors import forbidden

@api.route('/themes/')
def get_themes():
    themes = Themes.query.order_by(Themes.id)
    return jsonify({
        'name': '主题',
        'themes': [theme.to_json() for theme in themes]
    })

@api.route('/theme/<int:id>')
def get_theme(id):
    theme = Themes.query.filter_by(id=id).first_or_404()
    _news = theme.stories.order_by(News.id)
    return jsonify({
        'theme': theme.name,
        'description': theme.description,
        'news': [news.to_json_simple() for news in _news]
    })
