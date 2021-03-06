# Generated by Django 2.1.7 on 2019-04-22 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20190415_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='catalog.Product'),
        ),
        migrations.AlterField(
            model_name='productimageurl',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image_urls', to='catalog.Product'),
        ),
    ]
