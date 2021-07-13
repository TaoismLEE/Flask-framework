from flask import Blueprint

tsp = Blueprint('main', __name__)

from . import views, errors
