# Created urls module and Import path method from django's urls module. Also import views module
from django.urls import path
from . import views

'''
By convention have to have a urlpatterns, is a list of path object that takes an empty string which represents
the root url. Also pass index just as refference not the method as the second argument to map the views to url.
Also specify the name of module(index) with keyword:argument.
'''
# Add new path object to define new url parameter for movies/detail page
# And name space set for the movie/id url as movies_detail and for index page movies_index
# Use int: converter to convert movie_id to integer
# Instead define url's name with prefix app's name, let's define a know variable app_name and assing app'e name in this case, movies.
# and then delete 'movies_' from the url's name
app_name = 'movies'

urlpatterns = [
  path("", views.index, name="index"),
  # path("", views.index, name="movies_index"),
  path("<int:movie_id>", views.detail, name="detail")
  # path("<int:movie_id>", views.detail, name="movies_detail")
]
