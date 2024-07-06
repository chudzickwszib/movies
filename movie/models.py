from django.db import models
import csv
import datetime


# Create your models here.
class Movie:

    def __init__(self, tmdb_id, original_title, overview, popularity, release_date, vote_count, vote_average):
        self.tmdb_id = tmdb_id
        self.original_title = original_title
        self.overview = overview
        self.popularity = popularity
        self.release_date = release_date
        self.vote_count = vote_count
        self.vote_average = vote_average

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
