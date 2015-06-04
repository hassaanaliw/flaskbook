from flask.ext.login import LoginManager
import os
from flask import Flask
from flask_sslify import SSLify
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.markdown import Markdown

app = Flask(__name__)


if 'DYNO' in os.environ:
    app.config.from_object('config.ProductionConfig')
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    sslify = SSLify(app)
else:
    app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
db.create_all()
Markdown(app, extensions=['fenced_code'])

login_manager = LoginManager()
login_manager.init_app(app)

from app.user.views import users
from app.posts.views import posts

app.register_blueprint(users)
app.register_blueprint(posts)
login_manager.login_view = '/login'

