# Generated by Django 4.0.4 on 2022-06-06 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0008_remove_tierlist_rating_favorite_favorite_tier'),
    ]

    operations = [
        migrations.RenameField(
            model_name='favorite',
            old_name='tier',
            new_name='tier_rating',
        ),
    ]