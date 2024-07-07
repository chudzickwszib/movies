from django.db import migrations
from movie.models import Movie

import datetime
import csv


def load_initial_data(apps, schema_editor):
    movies_list = []
    with open('movie/migrations/movies_small.csv', 'r', encoding='utf-8') as all_movies_file:
        reader = csv.DictReader(all_movies_file, delimiter=',')

        for row in reader:
            movies_list.append(Movie(
                tmdb_id=row['tmdb_id'],
                original_title=row['original_title'],
                overview=row['overview'],
                popularity=row['popularity'],
                release_date=datetime.datetime.strptime(row['release_date'], '%m/%d/%Y'),
                vote_count=int(row['vote_count']),
                vote_average=float(row['vote_average']),
            ))

    Movie.objects.bulk_create(movies_list)


class Migration(migrations.Migration):
    initial = False

    dependencies = [
        ('movie', '0001_initial')
    ]

    operations = [
        migrations.RunPython(load_initial_data)
    ]
