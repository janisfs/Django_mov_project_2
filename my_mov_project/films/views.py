from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilmForm
from .models import Film


def index(request):
    return render(request, 'my_mov_project/index.html')


# Create your views here.
def films(request):
    films = Film.objects.filter(image__isnull=False)
    return render(request, 'films/films.html', {'films': films})


def add_film(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            error = 'Фильм успешно добавлен!'
            return redirect('films:films')
    else:
        form = FilmForm()
    return render(request, 'films/add_film.html', {'form': form, 'errors': error})



def films_detail(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    return render(request, 'films/film_detail.html', {'film': film})