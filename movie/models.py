from django.db import models
import csv
import datetime


# Create your models here.
class Movie(models.Model):
    tmdb_id = models.CharField(max_length=255)
    original_title = models.CharField(max_length=1000)
    overview = models.TextField()
    popularity = models.DecimalField(max_digits=20, decimal_places=10)
    release_date = models.DateField()
    vote_count = models.IntegerField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=2)
