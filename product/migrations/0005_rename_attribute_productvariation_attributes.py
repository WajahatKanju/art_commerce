# Generated by Django 4.2.4 on 2023-08-30 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_productvariation_attribute_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariation',
            old_name='attribute',
            new_name='attributes',
        ),
    ]
