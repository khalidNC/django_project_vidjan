from django.shortcuts import render
from django.http import HttpResponse

# Define views usally the function called index that represents the main page of an app
# When the request is sent to an address the the function is get called and returns response, this could be a text
# So we import HttpResponse class from django http module
def index(request):
  return HttpResponse("Hello Word")
