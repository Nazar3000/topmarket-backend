# Generated by Django 2.1.7 on 2019-04-17 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190417_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdelivery',
            name='place_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]