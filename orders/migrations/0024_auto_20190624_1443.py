# Generated by Django 2.1.7 on 2019-06-24 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20190516_1252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ продавца', 'verbose_name_plural': 'Заказы продавцов'},
        ),
    ]