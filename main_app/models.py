from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=100, blank = True, null = True)
    bgg_id = models.IntegerField(blank = True, null = True)
    thumbnail = models.CharField(max_length=250, blank = True, null = True)
    img = models.CharField(max_length=250, blank = True, null = True)
    description = models.CharField(max_length=10000, blank = True, null = True)
    year_published = models.IntegerField(blank = True, null = True)
    min_players = models.IntegerField(blank = True, null = True)
    max_players = models.IntegerField(blank = True, null = True)
    min_playtime = models.IntegerField(blank = True, null = True)
    max_playtime = models.IntegerField(blank = True, null = True)
    min_age = models.IntegerField(blank = True, null = True)
    # Needed for Game and TrendingGame to have the same URL for game_Detail views
    slug = models.SlugField(blank = True, null = True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game_detail", kwargs={"slug:": self.slug})
    
    class Meta:
        ordering = ['bgg_id']

class TrendingGame(models.Model):
    name = models.CharField(max_length=100, blank = True, null = True)
    bgg_id = models.IntegerField(blank = True, null = True)
    rank = models.IntegerField(blank = True, null = True)
    thumbnail = models.CharField(max_length=250, blank = True, null = True)
    year_published = models.IntegerField(blank = True, null = True)
    # Needed for Game and TrendingGame to have the same URL for game_Detail views
    slug = models.SlugField(blank = True, null = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("game_detail", kwargs={"slug:": self.slug})

    class Meta:
        ordering = ['rank']

class Collection(models.Model):
    name = models.CharField(max_length=100, blank = True, null = True)
    games = models.ManyToManyField(Game)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username

class Wishlist(models.Model):
    name = models.CharField(max_length=100, blank = True, null = True)
    games = models.ManyToManyField(Game)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user.username