# Generated by Django 4.2.1 on 2023-10-28 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
