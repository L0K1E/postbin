from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskapp.config import Config
from flask_mail import Mail
from flask_admin import Admin
from flask_whooshee import Whooshee
from newsapi import NewsApiClient

db = SQLAlchemy()
admin = Admin()
bcrypt = Bcrypt()
whooshee = Whooshee()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'danger'
mail = Mail()
newsapi = NewsApiClient(api_key='582e253204bc4247908077fd638501ff')


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    admin.init_app(app)
    bcrypt.init_app(app)
    whooshee.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskapp.main.routes import main
    from flaskapp.posts.routes import posts
    from flaskapp.users.routes import users
    from flaskapp.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
