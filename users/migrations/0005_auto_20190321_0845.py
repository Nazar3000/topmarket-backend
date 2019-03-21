# Generated by Django 2.1.7 on 2019-03-21 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190320_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1095, verbose_name='Имя сферы деятельности')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Company name')),
                ('areas_of_activity', models.TextField(blank=True, max_length=255, null=True, verbose_name='Сфера услуг')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='users/company/logos', verbose_name='Лого компании')),
                ('is_internet_shop', models.BooleanField(default=False, verbose_name='Интернет магазин')),
                ('is_offline_shop', models.BooleanField(default=False, verbose_name='Оффлайн-магазин')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1095, verbose_name='Name company type')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceIndustry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=1095, verbose_name='Name service industry')),
            ],
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='new_order_email',
            field=models.BooleanField(default=False, verbose_name='Новый заказ (email)'),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='new_order_tel',
            field=models.BooleanField(default=False, verbose_name='Новый заказ (смс)'),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='order_paid',
            field=models.BooleanField(default=False, verbose_name='Получение счета на оплату'),
        ),
        migrations.AlterField(
            model_name='usernotification',
            name='ttn_change',
            field=models.BooleanField(default=False, verbose_name='Смена ТТН заказа'),
        ),
    ]
