# Generated by Django 5.0.6 on 2024-08-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0004_remove_product_image_product_image1_product_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Highlights',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
