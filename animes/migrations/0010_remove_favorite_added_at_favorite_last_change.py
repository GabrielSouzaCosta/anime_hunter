# Generated by Django 4.0.4 on 2022-06-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0009_rename_tier_favorite_tier_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='added_at',
        ),
        migrations.AddField(
            model_name='favorite',
            name='last_change',
            field=models.DateTimeField(auto_now=True),
        ),
    ]