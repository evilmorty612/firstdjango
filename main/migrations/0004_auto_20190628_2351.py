# Generated by Django 2.2.2 on 2019-06-28 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190628_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tut',
            name='tut_publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 23, 51, 40, 214740), verbose_name='date published'),
        ),
    ]
