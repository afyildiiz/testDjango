from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_name = models.CharField(max_length=100)
    movie_category = models.CharField(max_length=100)
    movie_desc = models.TextField()
    in_homepage = models.BooleanField(default=False)
