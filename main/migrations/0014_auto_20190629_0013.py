# Generated by Django 2.2.2 on 2019-06-28 18:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20190629_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tut',
            name='tut_publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 29, 0, 13, 45, 719722), verbose_name='date published'),
        ),
    ]
