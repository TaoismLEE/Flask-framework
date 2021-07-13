import os

# Assign the absolute home path to basedir
basedir = os.path.abspath(os.path.dirname(__file__))


# Locate the common configures of project
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '12345678'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[TSP] - '
    FLASKY_MAIL_SENDER = 'xxxx@163.com'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'xxxx@163.com'
    MAIL_PASSWORD = 'xxxxx'

    @staticmethod
    def init_app(app):
        pass


# Inherit from Config class, and define specific configures for particular environment
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@172.20.10.2:3306/stock'


class TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@172.20.10.2:3306/stock'


class UAT(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@172.20.10.2:3306/stock'


class Production(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@172.20.10.2:3306/stock'


# Environment dict
config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'uat': UAT,
    'production': Production
}
