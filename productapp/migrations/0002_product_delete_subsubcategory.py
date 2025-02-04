# Generated by Django 5.0.6 on 2024-08-10 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(default='', upload_to='shop/product_images')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('minimum_order_quantity', models.PositiveIntegerField(default=1)),
                ('size', models.CharField(blank=True, max_length=255)),
                ('color', models.CharField(blank=True, max_length=255)),
                ('material', models.CharField(blank=True, max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('technical_specifications', models.TextField(blank=True)),
                ('customer_reviews', models.TextField(blank=True)),
                ('average_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('keywords', models.CharField(blank=True, max_length=255)),
                ('warranty_information', models.TextField(blank=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productapp.category')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='productapp.subcategory')),
            ],
        ),
        migrations.DeleteModel(
            name='SubSubCategory',
        ),
    ]
