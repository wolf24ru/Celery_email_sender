import time
from celery import Celery

from config import BROKER_URL, RESULT_BACKEND

app = Celery('tasks',
             backend=BROKER_URL,
             broker=RESULT_BACKEND)


@app.task()
def funcrion():
    pass