# Generated by Django 4.2.3 on 2023-08-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_eventdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetails',
            name='event_type',
            field=models.CharField(choices=[('Birthday', 'Birthday'), ('Work Anniversary', 'Work Anniversary'), ('No Events', 'No Events')], max_length=200, verbose_name='Event Title'),
        ),
    ]
