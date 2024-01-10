"""vidjan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

'''
Added a path object to tell vidjan app that path starts with 'movies/' should be headed off to 
the url config of movies app. So need to pass include method as 2nd argument that takes urls module from movies
so we import include class from django's urls module.
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls'))
]
