from django.contrib import admin
from movie.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_filter = ('vote_count', 'original_title')
    date_hierarchy = 'release_date'
    list_display = ('original_title', 'release_date', 'vote_count')


# Register your models here.
admin.site.register(Movie, MovieAdmin)
