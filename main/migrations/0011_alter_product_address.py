# Generated by Django 3.2 on 2024-01-18 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_alter_product_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="address",
            field=models.CharField(max_length=455),
        ),
    ]
