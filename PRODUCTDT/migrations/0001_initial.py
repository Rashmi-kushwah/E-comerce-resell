# Generated by Django 5.0.2 on 2024-04-03 15:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productdt',
            fields=[
                ('Product_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mrp', models.IntegerField()),
                ('sub_title', models.CharField(blank=True, max_length=30, null=True)),
                ('brand', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('Category', models.CharField(blank=True, max_length=20, null=True)),
                ('material', models.CharField(max_length=100)),
                ('sleeve_length', models.CharField(max_length=50)),
                ('neckline', models.CharField(max_length=50)),
                ('pattern', models.CharField(max_length=100)),
                ('occasion', models.CharField(max_length=100)),
                ('Model_name', models.CharField(blank=True, max_length=20, null=True)),
                ('img1', models.CharField(blank=True, max_length=200, null=True)),
                ('img2', models.CharField(blank=True, max_length=200, null=True)),
                ('img3', models.CharField(blank=True, max_length=200, null=True)),
                ('img4', models.CharField(blank=True, max_length=200, null=True)),
                ('img5', models.CharField(blank=True, max_length=200, null=True)),
                ('img6', models.CharField(blank=True, max_length=200, null=True)),
                ('img7', models.CharField(blank=True, max_length=200, null=True)),
                ('img8', models.CharField(blank=True, max_length=200, null=True)),
                ('size1', models.CharField(blank=True, max_length=50, null=True)),
                ('size2', models.CharField(blank=True, max_length=50, null=True)),
                ('size3', models.CharField(blank=True, max_length=50, null=True)),
                ('qty1', models.IntegerField()),
                ('qty2', models.IntegerField()),
                ('qty3', models.IntegerField()),
                ('qty4', models.IntegerField()),
                ('net_quantity', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
