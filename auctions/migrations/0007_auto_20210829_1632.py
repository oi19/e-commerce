# Generated by Django 3.1.7 on 2021-08-29 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210829_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 29, 16, 32, 0, 329395)),
        ),
    ]
