# Generated by Django 2.1.7 on 2019-04-25 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_orderuser_rozetka_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ttn',
            field=models.CharField(max_length=32, null=True),
        ),
    ]