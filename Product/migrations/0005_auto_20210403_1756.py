# Generated by Django 3.1.7 on 2021-04-03 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineCartApp', '0009_auto_20210403_1756'),
        ('Product', '0004_orders_orderprod'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='prodid',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='orderprod',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='productmeta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='OnlineCartApp.productsmeta'),
        ),
    ]