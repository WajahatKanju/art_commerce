# Generated by Django 4.2.4 on 2023-08-30 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_productvariation_attribute_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='attribute_values',
            field=models.ManyToManyField(related_name='attribute_values', to='product.attributevalue'),
        ),
    ]
