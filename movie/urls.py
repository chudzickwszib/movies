from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies, name='all_movies_url'),
    path('<id>', views.movie_details, name='movie_details_url'),
    path('add', views.add_movie, name='add_movie_url')
]
