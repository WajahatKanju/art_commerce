# Generated by Django 4.2.4 on 2023-08-30 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_productvariation_attribute_values_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute', to='product.attribute'),
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='attribute_value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute_values', to='product.attributevalue'),
        ),
    ]