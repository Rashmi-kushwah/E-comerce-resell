# Generated by Django 5.0.2 on 2024-04-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CARTPRODUCT', '0002_alter_addcart_product_id_alter_addcart_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcart',
            name='reselling_margin',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
