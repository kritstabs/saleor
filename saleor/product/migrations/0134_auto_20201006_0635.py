# Generated by Django 3.1 on 2020-10-06 06:35

from django.db import migrations, models


def migrate_visible_in_listings_and_available_for_purchase(apps, schema_editor):
    ProductChannelListing = apps.get_model("product", "ProductChannelListing")

    for channel_listing in ProductChannelListing.objects.iterator():
        product = channel_listing.product
        channel_listing.visible_in_listings = product.visible_in_listings
        channel_listing.available_for_purchase = product.available_for_purchase
        channel_listing.save(
            update_fields=["visible_in_listings", "available_for_purchase"]
        )


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0133_migrate_cost_price_to_channel_listing"),
    ]

    operations = [
        migrations.AddField(
            model_name="productchannellisting",
            name="visible_in_listings",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="productchannellisting",
            name="available_for_purchase",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.RunPython(
            migrate_visible_in_listings_and_available_for_purchase,
            migrations.RunPython.noop,
        ),
        migrations.RemoveField(model_name="product", name="visible_in_listings",),
        migrations.RemoveField(model_name="product", name="available_for_purchase",),
    ]