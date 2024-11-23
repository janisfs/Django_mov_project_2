import os
from django.db import models



# Create your models here.
class Film(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField()
    image = models.ImageField('Изображение', upload_to='films/', blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Comment(models.Model):
    author = models.CharField('Автор', max_length=100)
    text = models.TextField('Текст комментария')
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Фильм'
    )
    created_at = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )

    def __str__(self):
        return f'Комментарий от {self.author} к фильму {self.film.title}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']  # Добавим сортировку