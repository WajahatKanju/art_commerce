# Generated by Django 4.2.4 on 2023-08-29 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_remove_productprice_attributes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productprice',
            name='product_variation_option',
        ),
        migrations.AddField(
            model_name='productprice',
            name='product_variation',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.productvariation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productvariation',
            name='attributes',
            field=models.ManyToManyField(related_name='attributes', to='product.attribute', verbose_name='Available Attributes'),
        ),
        migrations.AddField(
            model_name='productvariation',
            name='colors',
            field=models.ManyToManyField(related_name='colors', to='product.color', verbose_name='Available Colors'),
        ),
        migrations.DeleteModel(
            name='ProductVariationOption',
        ),
    ]
