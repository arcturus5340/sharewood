# Generated by Django 2.2.2 on 2019-06-18 19:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_records_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]