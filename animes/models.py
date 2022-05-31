from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Favorite(models.Model):
    anime_id = models.IntegerField()
    name = models.CharField(max_length=200)
    image_url = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def is_in_user_list(self):
        item = Favorite.objects.filter(anime_id=self.anime_id, user=self.user_id).first()
        if item:
            return True
        else:
            return False

    def __str__(self):
        return self.name


class Watchlist_item(models.Model):
    anime_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image_url = models.TextField()
    watching = models.BooleanField(default=False)
    watched = models.BooleanField(default=False)
    user_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    added_at = models.DateTimeField(default=timezone.now)

    def is_in_user_list(self):
        item = Watchlist_item.objects.filter(anime_id=self.anime_id, user=self.user_id).first()
        if item:
            return True
        else:
            return False

    def __str__(self):
        return self.name




