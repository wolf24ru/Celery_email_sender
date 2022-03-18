from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from celeryapp import make_celery

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.POSTGRE_URI
app.config.update(CELERY_BROKER_URL=config.BROKER_URL,
                  CELERY_RESULT_BACKEND=config.RESULT_BACKEND)
celery = make_celery(app)
db = SQLAlchemy(app)
