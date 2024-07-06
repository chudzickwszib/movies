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

    @staticmethod
    def find_all_movies():
        movies_list = []

        with open('movie/migrations/movies_small.csv', 'r', encoding='utf-8') as all_movies_file:
            reader = csv.DictReader(all_movies_file, delimiter=',')

            for row in reader:
                movies_list.append(Movie(
                    row['tmdb_id'],
                    row['original_title'],
                    row['overview'],
                    row['popularity'],
                    datetime.datetime.strptime(row['release_date'], '%m/%d/%Y'),
                    int(row['vote_count']),
                    float(row['vote_average']),
                ))

        return movies_list
