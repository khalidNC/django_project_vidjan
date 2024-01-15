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
  # output = ', '.join([m.title for m in movies]). [We commented out becasue now we use render fuction to get html content]
  # return HttpResponse(output) [We commented out becasue now we use render fuction to get html content]

  # return result of render method and pass request object and template file and movies list context dictionary
  # Note: Created templates folder under movies app and added index.html file there
  # App-name specific html template adding movies/ prefix sicne we keep the template inside the movies folder
  return render(request, "movies/index.html", { "movies": movies })

# Define a view function detail for the movie detail page and initially retunrs httpresponse for the movie_id
def detail(request, movie_id):
  return HttpResponse(movie_id)
