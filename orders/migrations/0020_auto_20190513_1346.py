# Generated by Django 2.1.7 on 2019-05-13 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20190506_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contractororder',
            options={'verbose_name': 'Заказ поставщика', 'verbose_name_plural': 'Заказы поставщиков'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ партнера', 'verbose_name_plural': 'Заказы партнеров'},
        ),
    ]