# Generated by Django 2.1.7 on 2019-04-09 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mystore',
            name='company',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Company'),
            preserve_default=False,
        ),
    ]
