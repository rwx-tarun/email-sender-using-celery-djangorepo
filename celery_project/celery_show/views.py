from django.http import HttpResponse
from django.shortcuts import render
from .task import send_email_task, sleepy
from django.core.mail import send_mail
from .helper import send_email_without_celery

def show(request):
    # send_email_task()
    send_email_without_celery()
    return HttpResponse("hello")


