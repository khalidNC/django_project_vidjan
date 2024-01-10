# Created urls module and Import path method from django's urls module. Also import views module
from django.urls import path
from . import views

'''
By convention have to have a urlpatterns, is a list of path object that takes an empty string which represents
the root url. Also pass index just as refference not the method as the second argument to map the views to url.
Also specify the name of module(index) with keyword:argument.
'''
urlpatterns = [
  path("", views.index, name="index")
]