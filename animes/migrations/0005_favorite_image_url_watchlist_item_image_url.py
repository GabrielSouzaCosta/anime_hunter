# Generated by Django 4.0.4 on 2022-05-31 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0004_alter_watchlist_item_user_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='favorite',
            name='image_url',
            field=models.TextField(default='abc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist_item',
            name='image_url',
            field=models.TextField(default='asdasd'),
            preserve_default=False,
        ),
    ]