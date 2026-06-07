from django.urls import path

from cinema.views import (
    genre_list,
    genre_detail,
    actor_list,
    actor_detail,
    cinema_hall_list,
    cinema_hall_detail,
    movie_list,
    movie_detail,
)

urlpatterns = [
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("actors/", actor_list, name="actor-list"),
    path("actors/<int:pk>/", actor_detail, name="actor-detail"),
    path("cinema_halls/", cinema_hall_list, name="cinema-hall-list"),
    path("cinema_halls/<int:pk>/", cinema_hall_detail, name="cinema-hall-detail"),
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
]
