from django.db import models
from django.utils import timezone

# Added Genre class that derive Model class from model module to inherite the features and can override few of them
# Class attribute set as name of the genre using CharField class and set the lenght of charachter 255
class Genre(models.Model):
  name = models.CharField(max_length=255)

  # Define a str magic method to represent string of Genera class boject
  def __str__(self):
    return self.name

# Similarly Genre added a Movie class and set class attributes for data generation
class Movie(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True, null=True)
  release_year = models.IntegerField()
  number_in_stock = models.IntegerField()
  daily_rate = models.FloatField()
  # Use ForeignKey class to make relationship(each movie has a genre) between genre and movie
  # And if a genre is deleted all the movies under this genre will be deleted this called CASCADE
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
  date_created = models.DateTimeField(default=timezone.now)
  watch = models.URLField()

  # Define a str magic method to represent string of Move class boject and this Title display on the inner page as title
  def __str__(self):
    return self.title.upper()
