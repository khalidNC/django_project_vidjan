from django.shortcuts import render


# Define a view function for homepage that takes request
# this function retunrs the results of the render function which takes the request, and html template
def home(request):
  return render(request, "home.html")