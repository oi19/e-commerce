# Generated by Django 3.1.7 on 2021-09-02 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20210829_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 9, 2, 17, 54, 17, 937324)),
        ),
    ]