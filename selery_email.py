import asyncio

from celeryapp import make_celery
from email_sender import mail
from new_app import app

celery = make_celery(app)


@celery.task()
def send_mail():
    return asyncio.run(mail())
