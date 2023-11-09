from datetime import timezone
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import AddMovies
from .models import Movies

# Create your views here.
def add_movie(request):
    templateName='add_movie.html'
    if request.method == "POST":
        form = AddMovies(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        else:
            print(form.errors)
    else:
        form = AddMovies()
    return render(request, templateName, {'form': form})


def delete_movie(request,id):
        movie=Movies.objects.get(pk=id)
        movie.delete()
        return redirect('homepage')

def edit_movie(request,id):
     movie=Movies.objects.get(id=id)
     return render(request,"edit_movie.html", {'data':movie})


def update(request, id):
    movie_instance = Movies.objects.get(pk=id)

    if request.method == 'POST':
        form = AddMovies(request.POST, instance=movie_instance)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = AddMovies(instance=movie_instance)

    return render(request, 'edit_movie.html', {'form': form,'data':movie_instance})

def getHomepage(request):
    data={
        "movies":Movies.objects.all()
    }
    return render(request,"index.html",data)

def goFormPage(request):
    form = AddMovies()

    return render(request,"add_movie.html", {"form":form})