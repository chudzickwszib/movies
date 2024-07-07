from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies, name='all_movies_url'),
    path('add', views.add_movie, name='add_movie_url'),
    path('<int:id>', views.movie_details, name='movie_details_url'),
    path('collections', views.all_collections, name='all_collections_url'),
    path('collections/<int:id>', views.collection_details, name='collection_details_url')
]
