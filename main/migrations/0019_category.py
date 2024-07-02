# Generated by Django 3.2 on 2024-02-03 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0018_alter_product_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
    ]
