from django.shortcuts import render, redirect, get_object_or_404
from .forms import FilmForm
from .models import Film
from django.urls import reverse
from .forms import CommentForm
from .models import Comment
from django.views.generic import DetailView, FormView


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
    comments = film.comments.all()
    form = CommentForm()

    return render(request, 'films/film_detail.html', {
        'film': film,
        'comments': comments,
        'form': form,
        'test_message': 'Это тестовая строка'
    })


def add_comment(request, film_id):
    film = get_object_or_404(Film, id=film_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        # print(f"Получены данные формы: {request.POST}")  # отладочный вывод
        if form.is_valid():
            comment = form.save(commit=False)
            comment.film = film
            comment.save()
            # print(f"Комментарий сохранен: {comment.text}")  # отладочный вывод
        # else:
            # print(f"Ошибки формы: {form.errors}")  # отладочный вывод

    return redirect('films:film', film_id=film_id)



class FilmDetailView(DetailView):
    model = Film

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(film=self.object)
        return context