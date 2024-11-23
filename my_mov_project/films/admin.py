from django.contrib import admin
from .models import Film, Comment

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'film', 'created_at')
    list_filter = ('created_at', 'film')
    search_fields = ('author', 'text')