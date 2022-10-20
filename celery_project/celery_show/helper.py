from django.core.mail import send_mail

def send_email_without_celery():
    send_mail('NO CELERY DEMO',
        "message",
        'kacohe1454@24rumen.com',
        ['kacohe1454@24rumen.com'],
        fail_silently=False
        )
    return None