from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_debugtoolbar import DebugToolbarExtension
from flask_cache import Cache
from flask_admin.contrib.sqla import ModelView
import flask_whooshalchemyplus
from flask_bootstrap import Bootstrap
from flask_whooshalchemyplus import index_all

bootstrap = Bootstrap()
db = SQLAlchemy()
debug_toolbar = DebugToolbarExtension()
cache = Cache()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    flask_whooshalchemyplus.init_app(app)
    debug_toolbar.init_app(app)
    cache.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/1.0')

    return app
