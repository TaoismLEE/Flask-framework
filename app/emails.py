from flask_mail import Message
from flask import render_template
from . import mail
from config import Config


def send_email(subject, receivers, template, **kwargs):
    '''
    :param subject: mail subject
    :param receivers: receiver-list
    :param template: html template supported Jinjia2
    :param kwargs: key-words args for template use
    :return: None
    '''
    msg = Message(Config.FLASKY_MAIL_SUBJECT_PREFIX + subject, sender=Config.FLASKY_MAIL_SENDER, recipients=receivers)
    msg.html = render_template(template, **kwargs)
    mail.send(msg)
