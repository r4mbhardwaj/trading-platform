# Generated by Django 4.2.1 on 2023-06-18 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0004_stock_volatility'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WishlistStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlisted_by', to='market.stock')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
