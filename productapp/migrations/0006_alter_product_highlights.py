# Generated by Django 5.0.6 on 2024-08-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0005_product_highlights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Highlights',
            field=models.TimeField(blank=True, max_length=1000),
        ),
    ]
