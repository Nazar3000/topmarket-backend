# Generated by Django 2.1.7 on 2019-05-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20190502_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mystore',
            name='domain_subdomain',
            field=models.CharField(blank=True, choices=[('DM', 'Домен'), ('SDM', 'Поддомен')], max_length=2, null=True, verbose_name='Домен/поддомен'),
        ),
    ]
