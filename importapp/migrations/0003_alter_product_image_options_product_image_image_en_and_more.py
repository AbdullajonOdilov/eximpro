# Generated by Django 4.1.1 on 2023-03-29 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importapp', '0002_product_image_remove_product_image_product_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_image',
            options={'verbose_name': '3-mahsulot rasmlari', 'verbose_name_plural': 'B - 3-mahsulot rasmlari'},
        ),
        migrations.AddField(
            model_name='product_image',
            name='Image_en',
            field=models.ImageField(null=True, upload_to='product', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='product_image',
            name='Image_ru',
            field=models.ImageField(null=True, upload_to='product', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='product_image',
            name='Image_uz',
            field=models.ImageField(null=True, upload_to='product', verbose_name='Image'),
        ),
    ]