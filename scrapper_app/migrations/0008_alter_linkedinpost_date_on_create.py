# Generated by Django 3.2.16 on 2023-04-18 09:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('scrapper_app', '0007_auto_20230418_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkedinpost',
            name='date_on_create',
            field=models.DateField(default=datetime.datetime(2023, 4, 18, 9, 3, 5, 164054, tzinfo=utc), verbose_name='Date on Create'),
        ),
    ]