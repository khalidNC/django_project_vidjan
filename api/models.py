# Import ModelResource from the resources module from tastypie package
# Import Movie class from movies app, models module
from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Define model class for api it refers as resource this class derive from the bass resource class from tastypie
# Tastypie looks at inner class Meta so defined Meta class as well
# Set queryset as it just queries all the movies objects
# And set resource_name as ''movies' this what the api endpoint looks like. e.g /api/movies
class MovieResource(ModelResource):
  class Meta:
    queryset = Movie.objects.all()
    resource_name = 'movies'
    # Exclude date_created field
    excludes = ["date_created"]
