# Generated by Django 3.1.7 on 2021-08-29 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210826_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='username',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='reviews',
            name='username',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 29, 15, 31, 5, 121241)),
        ),
    ]