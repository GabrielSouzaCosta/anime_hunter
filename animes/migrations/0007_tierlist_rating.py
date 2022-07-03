# Generated by Django 4.0.4 on 2022-06-05 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animes', '0006_favorite_episodes_watched_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tierlist_rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.CharField(max_length=100)),
                ('favorite', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='animes.favorite')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]