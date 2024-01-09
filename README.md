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

## Step 1: Initial course of actions and directory structure:
1. Create a directory terminal command: 
***
    mkdir vidjan 
2. Go the directory and create virtual environment and install django: 
***
    cd vidjan
    pipenv install django==2.1
3. Create django project in current directory using django admin tool: 
***
    django-admin startproject vidjan .
4. Open the project in vscode: 
***
    code .
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
      ├── manage.py
      │
      ├── Pipfile
      └── Pipfile.lock
6. In vscode, select the python enterpretor and active the virtual environment.
7. Then let's run the server, terminal commandline: 
***
    python3 manage.py runserver
8. By default it is going to start at development server on port 8000 at an address like: http://127.0.0.1:8000/
11. Now just navigate to the address and it will open the page in a browser. And this is our Django project.

## Step 2: Creation of movies app in the project:
1. In Django, the project that contains multiple apps. The apps do not represent the entire application, they represent a small part of the application that focouse on one function area. Let's say we are going to build a website like Amazon. Amazon has a lot of different functional areas such as customer service, orders, shipping and so on. Each functional area includes a bunch of highly related functions. So with this architecture we can break down large complex project into a smaller, more manageable and more maintainable apps. Also we can reuse these apps in other Django projects. For example, we can build an app that represents a blog, and then reuse this app in an website that needs a blog. So here we are going to create a new app called movies, in this small app we are going to have all the functionality for displaying the list of all the movies as well as the details of a given movie.
2. Stop the development server and run this command in terminal: 
***
    python3 manage.py startapp movies
3. This creates a new directory 'movies' and what we have in the directory:
***
        a. migrations: a directory
        b. __init__.py: file to tell python to treate this as package
        c. admin.py: file this is where we difine how the adminstartion area for managing the movies
        d. apps.py: we use this to store various configaration settings for the app
        e. models.py: here we have models and we define classess that represents domain of the this app.
        g. test.py: here we write automated tests for the app
        h. views.py: is the module where we define our view functions
  
4. Directory structure at this point:
***
    VIDJAN/
      │
      ├── movies/
      │   ├── migrations/
      │   │   └── __init__.py
      │   ├── __init__.py
      │   ├── admin.py
      │   ├── apps.py
      │   ├── models.py
      │   ├── test.py
      │   └── views.py
      │
      ├── vidjan/
      │   ├── __init__.py
      │   ├── settings.py
      │   ├── urls.py
      │   └── wsgi.py
      │
      ├── manage.py
      │
      ├── Pipfile
      └── Pipfile.lock
## Step 3: Define views functions:
1. Go to the movies directory and open the views.py file
2. Define a function 'index'. This name is arbitrary, we could call it anything but usually we use the word index for naming the function that represents a main page of an app. For example, /movies app page when we send a request to the address to the endpoint our index function is going to get call. So index represents the main page of an app.
```python
      # Codes:
            from django.http import HttpResponse
            from django.shortcuts import render

            def index(request):
              return HttpResponse("Hello World")
```
## Step 4: Map the view function to a url in movies app:
1. Add a new py file by convention the name should be urls.py in movies directory.
2. Here create a variable urlpatterns and set a list here, again this is Django convetion to follow.
3. In this list, we add objects that can map url endpoints or view function.
4. And to do this we use path function in Django. So import path function from django.urls
5. Then we call path function to create path object in the list.
6. It takes two arguments:
***
        The first argument - should specify url endpoint:
          a. here we will pass an empty string. This represents the root of this app. 
          b. For exmple: in our movies app, we are going to have some url endpoints like,
                movies/ - this is root url
                movies/1/details - here we assume 1 is the id of a given movie
        The second argument - map this to a view function:
          a. To do so we need to import the index function that we created earlier. that is in our views module
          b. Look at the views.py file in the movies directory.
          c. 'import views' will not work in Django because this is how django loads the modules. 
          d. So we should use a relative import statement. 'from . import views'
          e. Back to the path function and pass a reference to a view function that is views.index
          f. Note: we do not call the index() function we just pass a reference to the index function.
7. At the run time when a user sends an http request to this(empty strint) endpoint then django will take care of calling this path function and give it an http request object. 
8. Also as a best practice we should name this url endpoint. So we pass a keyword=argument: name="index".
9. Now save the changes. So we have now:
***
          a. A defined variable urlpatterns
          b. That contains one or more path objects that map url endpoints to view functions.
```python
        # Codes:
              from . import views
              from django.urls import path

              urlpatterns = [
                path("", views.index, name="index"),
              ]
```
## Step 5: Map movies urls to the main app vidjan:
1. So we have done with the url configuration so far. But our main app, the vidjan app has no knowledge of the movies app. So if we head over to the local host port 8000/movies nothing will going to be happen. Our Django application is not aware of that.
2. Now we need to go to the main app, vidjan directory
3. here in the directory we see urls.py file, that defines the url configuration for our main app.
```python
        # Here in the file we see:
        # Codes:
              from django.contrib import admin
              from django.urls import path

              urlpatterns = [
                path("admin/", admin.site.urls),
              ]
        # a. By convention django looks for urlpatterns variable when starting our django project.
        # b. We have a path object that maps anything that starts with admin to admin.site.urls.
        # c. So every django project comes with an adminstrative panel that is a separate independent app.
```
4. Now add a new path object here to tell our Vidjan app:
***
        a. that any path starts with 'movies/' should be handed off to the url configuration in the 'movies' app.
        b. So here in the import statement(from django.urls import path) import another function called include.
        c. And as second argument we call the include() function.
        d. And pass a string("movies.urls") that contains the url configuration for the movies app.
        So whenever a request is sent that starts with 'movies' django will chop off the prefix("movies/") 
        and send the remaining string to this("movies.urls") module. That is the reason an empty string is used 
        in the url configuration for the movies app to represent the root of this app.
```python
        # Codes:
              from django.contrib import admin
              from django.urls import path, include

              urlpatterns = [
                path("admin/", admin.site.urls),
                path("movies/", include("movies.urls"))
              ]
```
5. Save the changes run the server and get page not found. but if you head over to /movies the 'Hello Word' text displays and that verifies it successfully mapped a url endpoint to a view function.

## Step 6: Models creations:
1. Models, the python classes that represents application data. Let's create two models, genre and movie in the movies app. models.py file:
```python
        # a. Create a class called genre and should derive this class from models.Model
                  # Codes: 
                          from django.db import models

                          class Genre(models.Model):

            '''
            Django has this package django.db that has all the functionalities 
            around working with database and has a module called models and this module 
            has a class called Model.

            So by inheriting the genre class from the base model class in django, the genre class also 
            inherites all the functionalities, which means we do not really have to write any code to store 
            genre objects in a database.

            The genre is movie's label or name of the type/category. So define a class attribute called name.
            And set it to an instance of a field class in django. So in the models module, we have 
            a bunch of field classes like, CharField to represent a database field that can contain textual 
            data, we also have IntegerField, FloatField, BooleanField and so on. So we have set this to an 
            instance of the CharField class. and pass keyword=argument max_length, let's set this to 255 
            characters.
            '''
                  Codes:
                        from django.db import models

                        class Genre(models.Model):
                          name = models.CharField(max_length=255)

        # b. So we have Genre class now create Movie class in same way and derive this class from models.model

                  # Codes:
                        from django.db import models

                        class Genre(models.Model):
                          name = models.CharField(max_length=255)

                        class Movie(models.Model):
            '''
            Now set attribute of a movie, in our imaginary video rental application, we need to know 
            the title of each movie, the year of realse, the number of these movie DVD's in stock, as well as 
            the daily rental rate. So let's create these attributes:
                1. We set the title as calling the function models.CharFields() and pass max_length
                2. Then set realse year as IntegerFields()
                3. Then numbers instock as IntegerFields()
                4. then daily rate as set as FloatFields()
            '''
                  Codes:
                        from django.db import models

                        class Genre(models.Model):
                          name = models.CharField(max_length=255)

                        class Movie(models.Model):
                          title = models.CharFields(max_length=255)
                          realse_year = models.IntegerFields()
                          number_in_stock = models.IntegerFields()
                          daily_rate = models.FloatFields()
```
2. Now each movie needs to be associated with a genre:
***
        a. Here we should add another attribute genre and set this to an instance of 
        models.ForeignKey() now with this we can create the relationship between movies and genaras.

        b. And as the first argument we need to pass the genre class because we want to add a 
        relationship between movies and genre class.

        c. And as the second argument we need to pass a keyword=argument that is on_delete and with this 
        we tell django what should happen when a genre is deleted. For example, if we have a genre called 
        comedy and we have 5 movies in this genre, what should happen if we delete comedy?

        d. Let's assume for this project if we delete a genre all the movies associated with this genre 
        will be deleted. This thing we called cascading. So here we set on_delete to models.CASCADE
```python
              # Codes:
                    from django.db import models

                    class Genre(models.Model):
                      name = models.CharField(max_length=255)

                    class Movie(models.Model):
                      title = models.CharFields(max_length=255)
                      realse_year = models.IntegerFields()
                      number_in_stock = models.IntegerFields()
                      daily_rate = models.FloatFields()
                      genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
```
        e. So up to this point we have two model classes that we need in the movies app. In the future, 
        we can come back and add additional classes or modify the existing ones. 

## Step 7: Synchronize database with model classes and Migration:
1. Store the model objects in our database:
      a. Sqlite3: Look at the db.sqlite3 file in the source directory. This is a blank sqlite database 
      that django automatically created.

      b. Open the db.sqlite3 file in DB Browser SQLite and there is no table yet. That means we need to 
      create a couple of tables. In order to store movies and generas in this database.

      c. Tables in sqlite: So every time we create new model classes or modified the existing one, we 
      tell django to compare our model classes with our database. Django will look at our database it 
      will figure out what tables and columns we have, then it will calculate the difference between 
      our model classes and our database tables. and based on that, it will create a migration, a 
      migration is essensially a python file that include some codes. When we run that it will 
      synchronize our database with our model classes. Let's take a look.
***
        i. Let's open the terminal
        ii. and run: python3 manage.py makemigrations
        iii. Then it shows innitially 'No changes detected'. Because by default django is not aware of 
        our model classes.
        iv. So first step is to register our movies app with django.
***
            Let's see how do this:
              1. In our project, inside the vidjan package, open settings.py this file contain various 
              configarations and settings. One of the settings is INSTALLED_APPS and few apps are 
              installed by default.
                    a. First one is admin: and this creates admin pannel for us
                    b. Then Auth: Which is authentication framework, with this we can authenticate users, 
                    and can see whochave the permission to perform various tasks.
                    c. Then contenttypes: A framework for creating generic relationship between model classes.
                    d. Sessions: This framework allows us to temporarily store data about the current users.
                    e. Messages: We have messaging framework, and use that in situation like when user creates 
                    new movie and we display the message like 'The movie is successfully created'.
                    f. Then staticfiles: Which is use for managing static files like css files, images and so on.

              2. Now we need to register our movies app here, so that django can keep track of our model classes 
              in that app.
                    a. So back to our movies folder and open the apps.py file
                    b. here we have various configaration settings for the movies app.
                    c. Look at the class name 'MoviesConfig' this class is in apps module of the movies package. 
                    So to register the movies app with django we need to provied the complete path of this class.
                    d. So bakc to the settings.py in vidjan package and we add MoviesConfig class full path first 
                    movies package then apps module then the class at the bottom. And save the changes.
```python
                          # Codes:
                                INSTALLED_APPS = [
                                  'django.contrib.admin',
                                  'django.contrib.auth',
                                  'django.contrib.contenttypes',
                                  'django.contrib.sessions',
                                  'django.contrib.messages',
                                  'django.contrib.staticfiles',
                                  'movies.apps.MoviesCongif'
                                ]
```
        v. Go back to the terminal again and run the makemigrations command once again:
                      python3 manage.py makemigrations
        vi. This time django has detected the changes in the movies app, so it created a migration that is 
        inside movies/migrations/0001_initial.py this file. 
        vii. Let's have a quick look at this migration in this file:
              1. Here we have class called Migration
              2. And in this class we have a couple of oparations for bringing our database up to date with 
              our current model classes. 
                  a. The first oparation: For creating a model we can see the name is set to genre. And the 
                  fields of genre are id and name. Note: In out code we only specify name not id, but 
                  django automatically creates this for us. And it ensures that every object has id property, 
                  that uniquely identifies that object. 

                  b. The secound oparations: In similarly we have another create model oparation for creating 
                  the movie table in this table we are going to have the files along with the id that we did 
                  not mention in our code but django takes care of this.
              3. Now this migration has not executed yet it simply describe the oparations that we need to be 
              perfomed in the database to brieng it up to date with our current model classes. 
              4. So next step is to run this migration:
                  a. Before run the migration let's see one thing;
                      - Open the terminal
                      - and run: python3 manage.py runserver
                      - OutPut: we see an error like, we have 16 unapplied migrations. This basically means, 
                      we have migrations that need to be executed. Eariler we had 15 unapplied now 16.
                      So let's stop server 'control c'
                  b. And run: python3 manage.py migrate
                      - This will run all the pending migrations we have. We can see all the migrations are 
                      applied.
                      - OutPut: As we can see each of migrations has a prefix with the name of the app that 
                      contains it.
                      - So here we have migration for contenttypes app, auth app, 3 migartions for admin app.
                      - After all the migartions at the bottopm we can see migartion for movies app.
              5. Now open the Sqlite databse once again, we can see we have a total numbers of tables. Each 
              of the tables is prefix with the name of the app that contains it. So we can see 2 tables for 
              movies app, movies_genera and movies_movie. And we can always overwrite anytime. If we expand 
              the move table we can see the columns, for id, realse date, and so on. So we do not have to 
              create any table manually, django does for us.
              6. We have also a table for django_migrations, django uses this for keeping track of the migrations 
              that are applied on the database.
              7. So go to browse data tab and select the django_migration table. And we see the list of all 
              migrations currently applied. If you scroll down and can see the migration for the move in the 
              list with it's name along with the date time.

## Step 8: Admin pannel:
1. 
              