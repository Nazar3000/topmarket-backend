# Generated by Django 2.1.7 on 2019-04-25 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_customuser_rozetka_old_orders_imported'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='rozetka_old_orders_imported',
        ),
    ]
