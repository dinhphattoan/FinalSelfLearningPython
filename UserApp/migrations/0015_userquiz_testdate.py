# Generated by Django 5.0 on 2024-01-07 08:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0014_remove_tmp_userquizquestionanswer_questions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquiz',
            name='testdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
