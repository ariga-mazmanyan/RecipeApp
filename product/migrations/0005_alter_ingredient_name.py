# Generated by Django 4.1.4 on 2023-01-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_recipe_id_ingredient_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
