from django.db import models
import os


# Create your models here.
class Film(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField()
    review = models.TextField('Отзыв', blank=True)
    image = models.ImageField('Изображение', upload_to='films/', blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


def film_image_path(instance, filename):
    # Заменяем пробелы на подчеркивания в имени файла
    filename = filename.replace(" ", "_")
    # Возвращаем путь, где файл будет сохранен
    return os.path.join('films', filename)