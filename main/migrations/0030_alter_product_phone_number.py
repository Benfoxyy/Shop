# Generated by Django 3.2 on 2024-02-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_product_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='phone_number',
            field=models.CharField(max_length=12),
        ),
    ]
