from django.shortcuts import render, redirect
from .models import Movie, MovieStatistics, MovieCollection
from django.http import HttpResponseNotFound
from django.db.models import Avg, Min, Max, Count
from .forms import MovieForm
from django.contrib.auth.models import User


# Create your views here.
def all_movies(request):
    title = request.GET.get('title')

    if title and len(title) > 3:
        found_movies = Movie.objects.filter(original_title__contains=title)
    else:
        found_movies = Movie.objects.all()[:25]

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
    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie_data = form.cleaned_data
            stats = MovieStatistics.objects.create(vote_count=0, vote_average=0, popularity=0)
            Movie.objects.create(
                tmdb_id=movie_data['tmdb_id'],
                original_title=movie_data['original_title'],
                overview=movie_data['overview'],
                release_date=movie_data['release_date'],
                cast=movie_data['cast'],
                genres=movie_data['genres'],
                keywords=movie_data['keywords'],
                director=movie_data['director'],
                statistics=stats
            )
            return redirect('all_movies_url')

    form = MovieForm()
    context = {
        'movie_form': form
    }
    return render(request, 'movie/add_movie.html', context)


def all_collections(request):
    user = User.objects.all()[0]
    movie_collections = MovieCollection.objects.filter(owner=user).annotate(movie_count=Count('movies'))
    context = {
        'collections': movie_collections
    }
    return render(request, 'movie/all_collections.html', context)
