from celery import shared_task
from time import sleep

from django.core.mail import send_mail 




@shared_task
def sleepy(duration):
    sleep(duration)
    return None



@shared_task
def send_email_task():
    send_mail('CELERY DEMO',
        'How are you',
        'tarun.singh@reyahealthcare.com',
        ['tarun6937@gmail.com'],
        fail_silently=False
    )
    return None
