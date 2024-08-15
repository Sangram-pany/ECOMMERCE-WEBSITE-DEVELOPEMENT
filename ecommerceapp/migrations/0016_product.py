# Generated by Django 5.0.6 on 2024-08-07 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0015_delete_contacus_remove_orderitems_order_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('category', models.CharField(default='', max_length=100)),
                ('subcategory', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=500)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
