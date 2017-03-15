from flask import jsonify, request, g, abort, url_for, current_app
from .. import db
from ..models import Stories, Dates
from . import api
from .errors import forbidden

@api.route('/date/<int:date>')
def get_date_stories(date):
    dates = Dates.query.filter_by(dates=str(date)).first_or_404()
    stories = dates.stories.order_by(Stories.id.desc())
    return jsonify({
        'date': date,
        'stories': [story.to_json_simple() for story in stories]
    })
