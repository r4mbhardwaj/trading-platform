# Generated by Django 4.2.1 on 2023-06-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_price_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='starting_price',
            field=models.FloatField(default=0),
        ),
    ]
