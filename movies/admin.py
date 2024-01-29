from django.contrib import admin
from .models import Genre, Movie

# Define a class to customize to show fields on the admin interface
class GenreAdmin(admin.ModelAdmin):
  list_display = ("id", "name")

class MovieAdmin(admin.ModelAdmin):
  # Change display item 'descriptopn' to 'truncated_description' to display in the list page
  list_display = ('id', 'title', 'truncated_description', 'release_year', 'number_in_stock', 'daily_rate', 'genre', 'date_created', 'watch')
  # Add search field option to search by title/description
  search_fields = ["title", "description"]
  # exclude = ('date_created', ) if we want to exclude any header from the list display
  
  # Define a function to truncate the description. This function check if the length is bigger than max length then the function truncate it returns.
  def truncated_description(self, obj):
    max_length = 20
    if len(obj.description) > max_length:
      return f'{obj.description[:max_length]}...'
    return obj.description
  
  # Set the column-name "Description" on the list page
  truncated_description.short_description = "Description"

# Register models here to show them in admin interface 
# so import Genre and Movie classes from models module in the current directory at the top
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
