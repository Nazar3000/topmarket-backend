# Generated by Django 2.1.7 on 2019-05-27 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0018_product_validated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='validated',
        ),
    ]
