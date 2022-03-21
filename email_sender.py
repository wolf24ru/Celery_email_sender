import asyncio
import aiosmtplib
from email.message import EmailMessage
from more_itertools import chunked

from models import User


def gen_emile_list():
    peoples = [person.email for person in User.query.all()]
    for person in peoples:
        yield person


async def send_email(email, text='next msg'):
    message = EmailMessage()
    message["From"] = "root@localhost"
    message["To"] = email
    message["Subject"] = 'New msg'
    message.set_content(text)

    await aiosmtplib.send(message, hostname="localhost", port=1020)


async def mail():
    for emails in chunked(gen_emile_list(), 10):
        email_tasks = [asyncio.create_task(send_email(email))
                       for email in emails]
        await asyncio.gather(*email_tasks)
