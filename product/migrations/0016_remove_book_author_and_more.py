# Generated by Django 4.2.4 on 2023-08-30 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_author_alter_productvariation_attribute_value_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RenameField(
            model_name='productvariation',
            old_name='attribute',
            new_name='attributes',
        ),
        migrations.AlterField(
            model_name='productvariation',
            name='attribute_value',
            field=models.ForeignKey(limit_choices_to={'attributes': 1}, on_delete=django.db.models.deletion.CASCADE, related_name='attribute_values', to='product.attributevalue'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
