# Generated by Django 3.1.7 on 2021-04-04 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineCartApp', '0009_auto_20210403_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='selectedqnt',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='availquantity',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='productsmeta',
            old_name='availquantity',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='cart',
            name='createddate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 12, 37, 49, 41975)),
        ),
    ]
