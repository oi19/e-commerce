# Generated by Django 3.1.7 on 2021-08-26 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210825_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 26, 13, 17, 55, 911779)),
        ),
    ]
