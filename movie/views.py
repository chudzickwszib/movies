from django.shortcuts import render
from .models import Movie


# Create your views here.
def all_movies(request):
    found_movies = Movie.find_all_movies()
    context = {
        'movies': found_movies
    }
    return render(request, 'movie/all_movies.html', context)
