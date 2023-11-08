from django import forms
from .models import Movies
# from movies.models import Movies

class AddMovies(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['movie_name', 'movie_category', 'movie_desc', 'in_homepage']
