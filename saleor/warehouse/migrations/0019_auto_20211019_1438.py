# Generated by Django 3.2.8 on 2021-10-19 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0038_merge_20210903_1048"),
        ("product", "0153_merge_20211006_0910"),
        ("warehouse", "0018_auto_20210323_2116"),
    ]

    operations = [
        migrations.CreateModel(
            name="PreorderReservation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity_reserved", models.PositiveIntegerField(default=0)),
                ("reserved_until", models.DateTimeField()),
                (
                    "checkout_line",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="preorder_reservations",
                        to="checkout.checkoutline",
                    ),
                ),
                (
                    "product_variant_channel_listing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="preorder_reservations",
                        to="product.productvariantchannellisting",
                    ),
                ),
            ],
            options={
                "ordering": ("pk",),
            },
        ),
        # nosemgrep: add-index-concurrently
        migrations.AddIndex(
            model_name="preorderreservation",
            index=models.Index(
                fields=["checkout_line", "reserved_until"],
                name="warehouse_p_checkou_3abf41_idx",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="preorderreservation",
            unique_together={("checkout_line", "product_variant_channel_listing")},
        ),
    ]
