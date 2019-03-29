# Generated by Django 2.1.7 on 2019-03-27 14:45

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='id - primary key')),
                ('name', models.CharField(max_length=256, verbose_name='Название категории')),
                ('slug', models.SlugField(allow_unicode=True, max_length=512, unique=True, verbose_name='Slug')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='ProductContractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('slug', models.SlugField(allow_unicode=True, max_length=511, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=255, verbose_name='Имя продукта')),
                ('vendor_code', models.CharField(max_length=63, verbose_name='Артикул')),
                ('brand', models.CharField(blank=True, max_length=255, null=True, verbose_name='Бренд')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Наличие')),
                ('description', models.TextField(blank=True, max_length=4095, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена товара')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Category', verbose_name='Категория товара')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductContractorImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='catalog/products/contractor/images', verbose_name='Изображение товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.ProductContractor')),
            ],
        ),
        migrations.CreateModel(
            name='ProductContractorImageURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Ссылка на изображение товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.ProductContractor')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('slug', models.SlugField(allow_unicode=True, max_length=511, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=255, verbose_name='Имя продукта')),
                ('vendor_code', models.CharField(max_length=63, verbose_name='Артикул')),
                ('brand', models.CharField(blank=True, max_length=255, null=True, verbose_name='Бренд')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Наличие')),
                ('description', models.TextField(blank=True, max_length=4095, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена товара')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Category', verbose_name='Категория товара')),
                ('partners', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.ProductContractor', verbose_name='партнеры')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductPartnerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='catalog/products/images', verbose_name='Изображение товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.ProductPartner')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPartnerImageURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Ссылка на изображение товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.ProductPartner')),
            ],
        ),
    ]
