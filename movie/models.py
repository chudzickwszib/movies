from django.db import models
from django.core.validators import MinValueValidator, RegexValidator, MaxValueValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(f'{value} nie jest liczbą parzystą')


class MovieStatistics(models.Model):
    popularity = models.DecimalField(max_digits=20, decimal_places=10, validators=[validate_even])
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    vote_average = models.DecimalField(max_digits=5, decimal_places=2,
                                       validators=[MinValueValidator(0), MaxValueValidator(10)])


# Create your models here.
class Movie(models.Model):
    tmdb_id = models.CharField(max_length=255, validators=[
        RegexValidator(r'tt\d{7}', message='Proszę podać poprawny TMDB ID')
    ])
    original_title = models.CharField(max_length=1000, validators=[MinLengthValidator(3)])
    overview = models.TextField(validators=[MinLengthValidator(10)])
    release_date = models.DateField()
    cast = models.CharField(max_length=1000, null=True)
    genres = models.CharField(max_length=1000, null=True)
    keywords = models.TextField(null=True)
    director = models.CharField(max_length=1000, null=True)
    statistics = models.OneToOneField(MovieStatistics, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.original_title}'


class MovieCollection(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    movies = models.ManyToManyField(Movie)
