# Generated by Django 5.0.2 on 2024-04-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_order_order_date_order_order_id_order_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Product_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
