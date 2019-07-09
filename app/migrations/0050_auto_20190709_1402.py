# Generated by Django 2.2.2 on 2019-07-09 14:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_auto_20190709_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='part_num',
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 9, 14, 2, 28, 66966)),
        ),
        migrations.AlterField(
            model_name='media',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 9, 14, 2, 28, 65471)),
        ),
        migrations.AlterField(
            model_name='revenue',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 9, 14, 2, 28, 67338)),
        ),
    ]
