from flask_sqlalchemy import SQLAlchemy
from flask import Flask

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.POSTGRE_URI
app.config.update(CELERY_BROKER_URL=config.BROKER_URL,
                  CELERY_RESULT_BACKEND=config.RESULT_BACKEND)
db = SQLAlchemy(app)
