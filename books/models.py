from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    vote_average = models.DecimalField(max_digits=5, decimal_places=2)
    vote_count = models.IntegerField()
    iban = models.CharField(max_length=10, null=True)
    publication_country = models.CharField(max_length=255, default='Polska')

    def __str__(self):
        return f'{self.title} ({self.publish_date})'

