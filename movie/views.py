from datetime import timezone
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import AddMovies
from .models import Movies

# Create your views here.
def add_movie(request):
    templateName='add_movie.html'
    print('1')
    if request.method == "POST":
        form = AddMovies(request.POST)
        if form.is_valid():
            print('2')
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


def getHomepage(request):
    data={
        "movies":Movies.objects.all()
    }
    return render(request,"index.html",data)

def goFormPage(request):
    form = AddMovies()

    return render(request,"add_movie.html", {"form":form})