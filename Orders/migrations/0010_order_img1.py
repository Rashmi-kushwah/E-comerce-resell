# Generated by Django 5.0.2 on 2024-05-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0009_order_total_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='img1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]