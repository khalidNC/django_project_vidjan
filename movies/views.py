# Import Movie class from models module from current directory
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

# Define views usally the function called index that represents the main page of an app
# When the request is sent to an address the the function is get called and returns response, this could be a text
# So we import HttpResponse class from django http module
def index(request):
  # Call all the movie object from database by database abstraction api and it returns movies object
  movies = Movie.objects.all()
  # Use list comprehention to retrive stirng out of the movie objects
  # Use comma separator join method to display all the movie titles on the /movies page
  output = ', '.join([m.title for m in movies])
  return HttpResponse(output)
