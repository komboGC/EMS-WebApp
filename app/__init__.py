# third-party imports
from flask import Flask, app
import flask_login
import flask_migrate
import flask_sqlalchemy
from flask_login import LoginManager
# local imports
from sqlalchemy.testing.pickleable import User

from config import app_config

# db variable initialization
db = flask_sqlalchemy.SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = flask_login.LoginManager()

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = flask_migrate.Migrate(app, db)
    from app import models

    from app import models

    from .admin import admin as admin_blueprint

    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .auth import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint

    app.register_blueprint(home_blueprint)

    return app
