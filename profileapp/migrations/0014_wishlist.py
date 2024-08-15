# Generated by Django 5.1 on 2024-08-13 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0008_alter_product_average_rating_alter_product_discount'),
        ('profileapp', '0013_alter_customer_mobileno_alter_shippingaddress_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileapp.customer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productapp.product')),
            ],
        ),
    ]
