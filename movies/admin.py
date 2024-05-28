from django.contrib import admin

# Register your models here.
from .models import Movie, Genre

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)