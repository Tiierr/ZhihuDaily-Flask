# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, SelectField
from wtforms.validators import Required, Length


class SearchForm(FlaskForm):
    search = StringField('', validators=[Required(),Length(0,64)])
    submit = SubmitField('搜索')
