# Generated by Django 2.2.2 on 2019-06-28 18:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tut_cat', models.CharField(max_length=200)),
                ('cat_sum', models.CharField(max_length=200)),
                ('cat_link', models.CharField(default=1, max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='tut',
            name='tut_link',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='tut',
            name='tut_publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 23, 43, 9, 143188), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tut_ser', models.CharField(max_length=200)),
                ('ser_summary', models.CharField(max_length=200)),
                ('tut_cat', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Cat', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'series',
            },
        ),
        migrations.AddField(
            model_name='tut',
            name='tut_ser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.Series', verbose_name='series'),
        ),
    ]
