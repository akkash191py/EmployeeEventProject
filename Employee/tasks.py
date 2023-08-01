from datetime import date
from django.core.mail import send_mail
from celery import shared_task
from Employee.models import Employee
from django.conf import settings
from django.db.models import Q


@shared_task
def send_birthday_anniversary_wishes():
    today = date.today()
    # users = Employee.objects.filter(
    #     Q(DOB__month=today.month, DOB__day=today.day) |
    #     Q(joining_date__month=today.month, joining_date__day=today.day)
    # )

    upcoming_birthdays = Employee.objects.filter(
            DOB__month=today.month,
            DOB__day=today.day
        )
    upcoming_anniversary = Employee.objects.filter(
        joining_date__month=today.month,
        joining_date__day=today.day
    )
    for user in upcoming_birthdays:
        birthDayWishes = "Dear" + user.first_name, + "Wishing you a great birthday and a memorable year, From all of us."
        send_mail(
            'Happy Birthday/Anniversary!',
            # f'Hi {user.first_name}, Happy Birthday!!',
            birthDayWishes,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    
    for userEvent in upcoming_anniversary:
        birthDayWishes = "Dear" + userEvent.first_name, + "Congratulations on your work anniversary! It’s a special day to celebrate your great work and dedication to your job over the years."
        send_mail(
            'Happy Birthday/Anniversary!',
            # f'Hi {user.first_name}, Happy Birthday!!',
            birthDayWishes,
            settings.EMAIL_HOST_USER,
            [userEvent.email],
            fail_silently=False,
        )