# Generated by Django 4.0.5 on 2022-08-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_comment_product_alter_productimage_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/articles/', verbose_name='Фото'),
        ),
    ]
