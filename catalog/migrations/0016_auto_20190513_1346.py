# Generated by Django 2.1.7 on 2019-05-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20190426_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=4095, null=True, verbose_name='Описание'),
        ),
    ]