from django import forms
from .models import Film

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'description', 'review', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите описание'}),
            'review': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отзыв'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }