from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from movies.models import Movie, Genre

class MovieAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_movies_list(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
