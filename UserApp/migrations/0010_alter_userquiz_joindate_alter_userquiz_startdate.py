# Generated by Django 5.0 on 2024-01-05 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0009_userquiz_quizscore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquiz',
            name='joindate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 7, 27, 1, 645920, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='userquiz',
            name='startdate',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 7, 27, 1, 645920, tzinfo=datetime.timezone.utc)),
        ),
    ]
