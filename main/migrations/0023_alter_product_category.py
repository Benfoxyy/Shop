# Generated by Django 3.2 on 2024-02-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.ManyToManyField(null=True, to='main.Category'),
        ),
    ]