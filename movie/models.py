from django.db import models
from django.core.validators import MinValueValidator, RegexValidator, MaxValueValidator, MinLengthValidator
from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(f'{value} nie jest liczbą parzystą')


# Create your models here.
class Movie(models.Model):
    tmdb_id = models.CharField(max_length=255, validators=[
        RegexValidator(r'tt\d{7}', message='Proszę podać poprawny TMDB ID')
    ])
    original_title = models.CharField(max_length=1000, validators=[MinLengthValidator(3)])
    overview = models.TextField(validators=[MinLengthValidator(10)])
    popularity = models.DecimalField(max_digits=20, decimal_places=10, validators=[validate_even])
    release_date = models.DateField()
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    vote_average = models.DecimalField(max_digits=5, decimal_places=2,
                                       validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f'{self.original_title}'
