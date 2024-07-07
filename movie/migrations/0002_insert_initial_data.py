from django.db import migrations
from movie.models import Movie, MovieStatistics

import datetime
import csv


def load_initial_data(apps, schema_editor):
    with open('movie/migrations/movies_small.csv', 'r', encoding='utf-8') as all_movies_file:
        reader = csv.DictReader(all_movies_file, delimiter=',')

        for row in reader:
            statistics = MovieStatistics(vote_count=int(row['vote_count']), vote_average=float(row['vote_average']),
                                         popularity=row['popularity'], )
            statistics.save()
            Movie.objects.create(
                tmdb_id=row['tmdb_id'],
                original_title=row['original_title'],
                overview=row['overview'],
                release_date=datetime.datetime.strptime(row['release_date'], '%m/%d/%Y'),
                statistics=statistics
            )


class Migration(migrations.Migration):
    initial = False

    dependencies = [
        ('movie', '0001_initial')
    ]

    operations = [
        migrations.RunPython(load_initial_data)
    ]
