# Generated by Django 3.2 on 2024-01-18 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_alter_product_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
