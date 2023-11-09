from django.contrib import admin
from django.urls import include, path

from .views import getHomepage,goFormPage
from movie import views

urlpatterns = [
    path("", views.getHomepage, name='homepage'),
    path("home/", views.getHomepage, name='homepage'),
    path("add/", views.add_movie, name='add',),
    path('update/<int:id>/', views.update, name='update'),
    # path("edit/<int:id>", views.edit_movie, name='edit',),
    path("__debug__/", include("debug_toolbar.urls")),
    # path('add_movie/', views.add_movie, name='add_movie'),
    path("delete/<int:id>", views.delete_movie, name='delete')
    
]