# Generated by Django 4.0.4 on 2022-05-31 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0005_favorite_image_url_watchlist_item_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='episodes_watched',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist_item',
            name='episodes_watched',
            field=models.IntegerField(default=0),
        ),
    ]
