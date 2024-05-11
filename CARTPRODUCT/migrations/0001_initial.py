# Generated by Django 5.0.2 on 2024-04-04 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addcart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.CharField(max_length=50)),
                ('user_uid', models.CharField(max_length=50)),
                ('sku_code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=50)),
                ('img1', models.CharField(max_length=200)),
                ('qty', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('mrp', models.IntegerField()),
                ('delivery_charges', models.CharField(max_length=30)),
                ('discount', models.CharField(max_length=30)),
                ('total_amount', models.CharField(max_length=30)),
                ('total_qty', models.CharField(max_length=30)),
            ],
        ),
    ]