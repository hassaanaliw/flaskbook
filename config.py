import os


class Config(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = "PLEASE_CHANGE_BEFORE_DEPLOYMENT"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db"