from django.test import TestCase

from . models import Genre, Movie

class GenreTestCase(TestCase):
    def test_model_field(self):
        obj = Genre.objects.create(name="Test")
        self.assertEqual(obj.name, "Test")

class MovieTestCase(TestCase):
    def test_movie_creation(self):
        genre = Genre.objects.create(name="Action")
        obj = Movie.objects.create(title="The Run", description="Indian action movie", release_year="1998", number_in_stock=1, daily_rate=1, genre=genre, date_created="2024-02-17", watch="www.youtube.com")
        self.assertEqual(obj.title, "The Run")
        self.assertEqual(obj.description, "Indian action movie")
        self.assertEqual(obj.release_year, "1998")
        self.assertEqual(obj.number_in_stock, 1)
        self.assertEqual(obj.daily_rate, 1)
        self.assertEqual(obj.genre, genre)
        self.assertEqual(obj.date_created, "2024-02-17")
        self.assertEqual(obj.watch, "www.youtube.com")
