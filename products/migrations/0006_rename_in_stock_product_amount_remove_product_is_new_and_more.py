# Generated by Django 4.0.5 on 2022-08-18 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_orderitem_ordered_orderitem_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='in_stock',
            new_name='amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='is_new',
        ),
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.IntegerField(default=0, verbose_name='Продано'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.category', verbose_name='Категория'),
        ),
    ]
