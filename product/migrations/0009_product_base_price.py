# Generated by Django 4.2.4 on 2023-08-30 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_productvariation_attribute_values'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=40.0, max_digits=8),
            preserve_default=False,
        ),
    ]
