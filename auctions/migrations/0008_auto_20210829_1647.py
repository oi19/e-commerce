# Generated by Django 3.1.7 on 2021-08-29 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210829_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 8, 29, 16, 47, 1, 928332)),
        ),
    ]