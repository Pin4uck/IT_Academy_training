from .models import Notes
from django.forms import ModelForm, TextInput, DateTimeInput, SlugField, Textarea


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'slug', 'content', 'data']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название записи'
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название slug'
            }),
            'content': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Контент записи'
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
        }
