# Generated by Django 4.2.2 on 2023-06-19 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verditown', '0002_producto_stock_alter_producto_precio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='SKU'),
        ),
    ]
