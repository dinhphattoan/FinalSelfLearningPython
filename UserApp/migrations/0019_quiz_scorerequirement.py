# Generated by Django 5.0 on 2024-01-10 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0018_userquiz_quizisover'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='scorerequirement',
            field=models.IntegerField(default=0),
        ),
    ]