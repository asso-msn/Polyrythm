import logging
import importlib
import os
from flask import Blueprint, Flask
from flask_assets import Environment
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .reporting import WebhookHandler

assets = Environment()
db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
moment = Moment()

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)s] %(name)s:\n%(message)s\n')
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    handler = WebhookHandler()
    handler.setLevel(logging.WARNING)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()

def init_blueprint(module, prefix=False, **kwargs):
    name = module[len(__name__) + 1:]
    if prefix:
        kwargs['url_prefix'] = '/' + module.split('.')[-1]
    return Blueprint(name, module,
        static_folder='static',
        template_folder='templates',
        **kwargs,
    )

def create_app(config_path='app.cfg'):
    os.environ['CONFIG_FILE'] = os.environ.get('CONFIG_FILE', config_path)
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config.from_envvar('CONFIG_FILE', True)
    login.init_app(app)
    assets.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    migrate.init_app(app, db)

    for module in ['admin', 'auth', 'main']:
        module = importlib.import_module(f'{__name__}.{module}')
        app.register_blueprint(module.bp)

    return app
