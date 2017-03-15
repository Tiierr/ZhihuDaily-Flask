from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import Stories
from . import api
from .errors import forbidden

@api.route('/stories/')
def get_stories():
    """
    ..  note:: 获取所有 stories

        1. 获取数据库中的所有 stories 数据
        2. 分页
        3. 响应格式为 json

    """
    count = current_app.config['FLASKY_JSONS_PER_PAGE']
    page = request.args.get('page', 1, type=int)
    pagination = Stories.query.paginate(
        page, per_page=count,
        error_out=False)
    stories = pagination.items
    prev = None
    if pagination.has_prev:
        prev = url_for('api.get_stories', page=page-1, _external=True)
    next = None
    if pagination.has_next:
        next = url_for('api.get_stories', page=page+1, _external=True)
    return jsonify({
        'count': count,
        'start': (page - 1) * int(count),
        'total': pagination.total,
        'prev': prev,
        'next': next,
        'stories': [story.to_json() for story in stories]
    })

@api.route('/story/<int:id>')
def get_story(id):
    """
    ..  note:: 获取指定的 movie 资源, 响应格式为 json
    """
    story = Stories.query.get_or_404(id)
    return jsonify(story.to_json())
