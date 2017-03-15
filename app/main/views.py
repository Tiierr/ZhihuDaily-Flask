from . import main
from flask import render_template, request, current_app
from ..models import Stories, Sections, News, Sections, Themes
from bs4 import BeautifulSoup
from app import cache
from .forms import SearchForm

cache.cached(timeout=60)
@main.route('/', methods=['GET'])
def index():
    page = request.args.get('page',1,type=int)
    pagination = Stories.query.order_by(Stories.id.desc()).paginate(
            page,per_page=current_app.config['DAILY_STORYS_PER_PAGE'],
            error_out=False)
    stories = pagination.items
    return render_template('index.html', stories=stories, pagination=pagination)


@main.route('/themes', methods=['GET'])
def themes():
    page = request.args.get('page',1,type=int)
    pagination = Themes.query.order_by(Themes.id).paginate(
            page,per_page=current_app.config['DAILY_THEMES_PER_PAGE'],
            error_out=False)
    themes = pagination.items
    return render_template('themes.html', themes=themes, pagination=pagination)


@main.route('/theme/<id>', methods=['GET'])
def theme(id):
    theme = Themes.query.filter_by(id=id).first_or_404()
    page = request.args.get('page',1,type=int)
    pagination = theme.stories.order_by(News.id).paginate(
            page,per_page=current_app.config['DAILY_THEME_ITEMS_PER_PAGE'],
            error_out=False)
    news = pagination.items
    return render_template('theme.html', theme=theme, news=news, pagination=pagination)


@main.route('/sections', methods=['GET'])
def sections():
    page = request.args.get('page',1,type=int)
    pagination = Sections.query.order_by(Sections.id).paginate(
            page,per_page=current_app.config['DAILY_SECTIONS_PER_PAGE'],
            error_out=False)
    sections = pagination.items
    return render_template('sections.html', sections=sections, pagination=pagination)

@main.route('/section/<id>', methods=['GET'])
def section(id):
    section = Sections.query.filter_by(id=id).first_or_404()
    page = request.args.get('page',1,type=int)
    pagination = section.stories.order_by(News.id).paginate(
            page,per_page=current_app.config['DAILY_SECTION_ITEMS_PER_PAGE'],
            error_out=False)
    news = pagination.items
    return render_template('section.html', section=section, news=news, pagination=pagination)

@main.route('/story/<id>', methods=['GET'])
def story(id):
    story = Stories.query.filter_by(id=id).first_or_404()
    return render_template('story.html', story=story)

@main.route('/news/<id>', methods=['GET'])
def new(id):
    story = News.query.filter_by(id=id).first_or_404()
    return render_template('story.html', story=story)

@main.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        page = request.args.get('page',1,type=int)
        pagination = News.query.whoosh_search(form.search.data).paginate(
                page,per_page=current_app.config['DAILY_STORYS_PER_PAGE'],
                error_out=False)
        stories = pagination.items
        return render_template('search-result.html', stories=stories, pagination=pagination)
    return render_template('search.html', form=form)
