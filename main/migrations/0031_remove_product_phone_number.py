# Generated by Django 3.2 on 2024-03-21 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_product_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='phone_number',
        ),
    ]
