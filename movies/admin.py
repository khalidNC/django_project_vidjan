from django.contrib import admin
from .models import Genre, Movie

# Define a class to customize to show fields on the admin interface
class GenreAdmin(admin.ModelAdmin):
  list_display = ("id", "name")

class MovieAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'release_year', 'number_in_stock', 'daily_rate', 'genre', 'date_created')
  # exclude = ('date_created', )

# Register models here to show them in admin interface 
# so import Genre and Movie classes from models module in the current directory at the top
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
