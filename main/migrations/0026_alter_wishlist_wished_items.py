# Generated by Django 3.2 on 2024-02-04 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='wished_items',
            field=models.ManyToManyField(blank=True, to='main.Product'),
        ),
    ]
