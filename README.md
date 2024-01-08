# Simple Web Application with Django
***
This is a test purpose simple web application build with Django frame work in Python3. This is a imaginary video rental store that rents movie's DVDs.

## The Features of this application as below:
1. Home page with list of movies
2. Landing paegs with movies detail
3. Api - the api will return the list of movies in json
4. And will deploy this to a cloud platform called Heroku

So we will going to see the process of building a web application from A to Z.

## Prerequisites for the project:
1. Python3
2. Django version 2.1
3. DB Browser for SQLite

## Initial steps of action and directory structure:
1. Create a directory terminal command: mkdir vidjan 
2. Go the directory and create virtual environment and install django: pipenv install django==2.1
3. Create django project in current directory using django admin tool: django-admin startproject vidjan .
4. Open the project in vscode: code .
5. This automatically created vidjan package and few modules and the directory structure looks now:
***
      VIDJAN/
      │
      ├── vidjan/
      │   ├── __init__.py
      │   ├── settings.py
      │   ├── urls.py
      │   └── wsgi.py
      │
      ├── venv/
      │   ├── Pipfile
      │   ├── Pipfile.lock
      │
      └── manage.py
6. In vscode, select the python enterpretor and active the virtual environment.
7. Then let's run the server, terminal commandline: python3 manage.py runserver
8. By default it is going to start at development server on port 8000 at an address like: http://127.0.0.1:8000/
11. Now just navigate to the address and it will open the page in a browser. And this is our Django project.

## Creation of app in the project:
1. In Django, the project that contains multiple apps. The apps do not represent the entire application, they represent a small part of the application that focouse on one function area. Let's say we are going to build a website like Amazon. Amazon has a lot of different functional areas such as customer service, orders, shipping and so on. Each functional area includes a bunch of highly related functions. So with this architecture we can break down large complex project into a smaller, more manageable and more maintainable apps. Also we can reuse these apps in other Django projects. For example, we can build an app that represents a blog, and then reuse this app in an website that needs a blog. So here we are going to create a new app called movies, in this small app we are going to have all the functionality for displaying the list of all the movies as well as the details of a given movie.
2. 