from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_movies, name='all_movies_url')
]
