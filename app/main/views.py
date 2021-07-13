from datetime import datetime
from .. import db
from ..emails import send_email
from . import tsp
from flask import session, render_template, url_for, redirect

# import forms based on flask-wtf
# from .forms import LoginForm

# import Models based on ORM
# from ..models import Roles, Users


@tsp.route('/', methods=['GET', 'POST'])
def index():
    send_email('ForTest', ['564735984@qq.com'], 'emails/email_template.html', name='test name')
    return render_template('index.html'), 200
