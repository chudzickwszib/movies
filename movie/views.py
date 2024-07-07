from django.shortcuts import render
from .models import Movie
from django.http import HttpResponseNotFound
from django.db.models import Avg, Min, Max, Count


# Create your views here.
def all_movies(request):
    title = request.GET.get('title')

    if title and len(title) > 3:
        found_movies = Movie.objects.filter(original_title__contains=title)
    else:
        found_movies = Movie.objects.all()

    found_movies_aggregation = found_movies.aggregate(Avg('statistics__vote_average'), Min('statistics__vote_average'),
                                                      Max('statistics__vote_average'), Count('id'))
    context = {
        'movies': found_movies,
        'aggregation_data': found_movies_aggregation,
        'filter_title': title
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


def add_movie(request):
    return render(request, 'movie/add_movie.html')
