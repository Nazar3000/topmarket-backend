# Generated by Django 2.1.7 on 2019-04-17 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190417_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
