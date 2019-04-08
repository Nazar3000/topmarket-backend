# Generated by Django 2.1.7 on 2019-04-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_ymltemplate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ymltemplate',
            name='id',
        ),
        migrations.AlterField(
            model_name='ymltemplate',
            name='yml_type',
            field=models.CharField(choices=[('rozetka', 'Rozetka'), ('prom', 'Prom')], max_length=10, primary_key=True, serialize=False),
        ),
    ]
