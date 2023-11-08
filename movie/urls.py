from django.contrib import admin
from django.urls import include, path

from .views import getHomepage,goFormPage
from movie import views

urlpatterns = [
    path("", views.getHomepage, name='homepage'),
    path("home/", views.getHomepage, name='homepage'),
    path("add/", views.goFormPage, name='add',),
    path("__debug__/", include("debug_toolbar.urls")),
    
]