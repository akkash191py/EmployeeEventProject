from datetime import date
from django.core.mail import send_mail
from celery import task
from .models import User
from django.conf import settings


@task
def send_birthday_anniversary_wishes():
    today = date.today()
    users = User.objects.filter(
        models.Q(DOB__month=today.month, DOB__day=today.day) |
        models.Q(joining_date__month=today.month, joining_date__day=today.day)
    )
    for user in users:
        send_mail(
            'Happy Birthday/Anniversary!',
            f'Hi {user.name}, Happy Birthday/Anniversary!',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )