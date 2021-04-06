# Generated by Django 3.1.7 on 2021-04-05 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineCartApp', '0011_auto_20210405_0847'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='cartuser',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='createddate',
        ),
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 5, 11, 2, 1, 557043)),
        ),
    ]