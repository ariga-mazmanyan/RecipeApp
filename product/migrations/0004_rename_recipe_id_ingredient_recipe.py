# Generated by Django 4.1.4 on 2023-01-19 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_recipe_ingredient_recipe_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='recipe_id',
            new_name='recipe',
        ),
    ]
