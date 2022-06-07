from time import sleep
from celery import shared_task

@shared_task
def print_something(message):
    print('Sending emails...')
    print(message)
    sleep(10)
    print('emails successfully sent')