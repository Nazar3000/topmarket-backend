# Generated by Django 2.1.7 on 2019-04-08 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='catalog.Category')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создание')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('availability', models.CharField(choices=[('NOT_AVAILABLE', 'Нет в наличии'), ('EXPECTED_DELIVERY', 'Ожидается поставка'), ('CAUSED', 'Вызывается'), ('IS_ENDING', 'Заканчивается'), ('IN_STOCK', 'В наличии'), ('IN_ARCHIVE', 'В архиве'), ('NOT_IN_STOCK', 'Нет на складе'), ('HIDDEN', 'Скрытый')], default='IN_STOCK', max_length=13, verbose_name='Доступность товара')),
                ('slug', models.SlugField(allow_unicode=True, max_length=511, unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=255, verbose_name='Имя продукта')),
                ('vendor_code', models.CharField(max_length=63, verbose_name='Артикул')),
                ('product_code', models.CharField(max_length=63, verbose_name='Код товара')),
                ('brand', models.CharField(blank=True, max_length=255, null=True, verbose_name='Бренд')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Наличие')),
                ('description', models.TextField(blank=True, max_length=4095, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена товара')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Category', verbose_name='Категория товара')),
                ('contractor_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contractor_products', to='catalog.Product', verbose_name='Связь с поставщиком продукта')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='catalog/products/images', verbose_name='Изображение товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImageURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='Ссылка на изображение товара')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
        ),
        migrations.CreateModel(
            name='YMLTemplate',
            fields=[
                ('template', models.FileField(upload_to='yml_templates')),
                ('yml_type', models.CharField(choices=[('rozetka', 'Rozetka'), ('prom', 'Prom')], max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'YML шаблон',
                'verbose_name_plural': 'YML шаблоны',
            },
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('user', 'contractor_product', 'vendor_code', 'product_code')},
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('parent', 'slug')},
        ),
    ]