from django.db import models
from django.utils import timezone

class Genera(models.Model):
  name = models.CharField(max_length=255)

class Movie(models.Model):
  title = models.CharField(max_length=255)
  release_year = models.IntegerField()
  number_in_stock = models.IntegerField()
  daily_rate = models.FloatField()
  genera = models.ForeignKey(Genera, on_delete=models.CASCADE)
  date_created = models.DateTimeField(default=timezone.now)
