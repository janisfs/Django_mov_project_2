from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.films, name='films'),  # главная страница
    path('film/<int:film_id>/', views.films_detail, name='film'),  # страница с детальной информацией о фильме
    path('add/', views.add_film, name='add_film'),  # страница добавления фильма
    path('film/<int:film_id>/add_comment/', views.add_comment, name='add_comment'),  # добавление комментария
]
