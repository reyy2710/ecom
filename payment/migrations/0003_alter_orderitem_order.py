# Generated by Django 5.0.6 on 2024-08-02 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0002_order_orderitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="order_items",
                to="payment.order",
            ),
        ),
    ]
