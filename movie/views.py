from django.shortcuts import render
from .models import Movie
from django.http import HttpResponseNotFound


# Create your views here.
def all_movies(request):
    found_movies = Movie.find_all_movies()
    context = {
        'movies': found_movies
    }
    return render(request, 'movie/all_movies.html', context)


def movie_details(request, tmdb_id):
    found_movie = Movie.find_all_movies()
    for m in found_movie:
        if m.tmdb_id == tmdb_id:
            context = {
                'movie': m
            }
            return render(request, 'movie/movie_details.html', context)
    return HttpResponseNotFound('Film nie został znaleziony')
