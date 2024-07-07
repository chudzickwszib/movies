from django.shortcuts import render
from .models import Movie
from django.http import HttpResponseNotFound


# Create your views here.
def all_movies(request):
    found_movies = Movie.objects.all()
    context = {
        'movies': found_movies
    }
    return render(request, 'movie/all_movies.html', context)


def movie_details(request, id):
    found_movie = Movie.objects.get(pk=id)
    if not found_movie:
        return HttpResponseNotFound('Film nie został znaleziony')
    context = {
        'movie': found_movie
    }
    return render(request, 'movie/movie_details.html', context)
