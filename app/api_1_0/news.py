from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import News
from . import api
from .errors import forbidden


@api.route('/news/<int:id>')
def get_news(id):
    news = News.query.get_or_404(id)
    return jsonify(news.to_json())
