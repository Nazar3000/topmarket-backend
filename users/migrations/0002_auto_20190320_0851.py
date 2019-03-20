# Generated by Django 2.0.13 on 2019-03-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='First name'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Last name'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='patronymic',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Patronymic'),
        ),
    ]
