from flask import Flask
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config
import pymysql

pymysql.install_as_MySQLdb()
moment = Moment()
db = SQLAlchemy()
mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    moment.init_app(app)
    db.init_app(app)
    mail.init_app(app)

    # Import blueprint and register to APP
    from .main import tsp
    app.register_blueprint(tsp)

    return app
