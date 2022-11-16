## Installing Django and Setting up the app;
>  pip3 install 'django<4'

>  pip install --upgrade pip
## Create a project;
>  django-admin startproject django_recipes .
## Check that the project server is working;
> python3 manage.py runserver
## Create a new app;
>  manage.py startapp recipes 

- In 'django_recipes/settings.py' add the app (recipes) to the INSTALLED_APPS dictionary.

## Create first view and url;
- In recipes/views.py import 'HttpResponse package' and create a function that allows a view for the user, for example;

- Create a file in recipes folder called urls.py (so we can work primarily from the app folder) and import views.py from the same file, "from . import views"
- Back in urls.py in django_recipes import the package "include" and create another path - "path('', include('recipes.urls'))" and what this is basically saying is when ever anyone goes to my app website "/" anything go to recipes.urls and use those url paths.
- Create a new url path in recipes/urls.py;
urlpatterns = [
    path('', views.home, name="recipes-home"),
]
- Run server to check it is working! 
> python3 manage.py runserver

## Create HTML templates 
- Create a 'templates' folder in 'recipes' folder, create another folder called 'recipes' in 'templates', and then in that, create a file called 'home.html'.
- In views.py add to the 'home' function - "return render(request, "recipes/home.html")" and delete the return of the HttpResponse. 

### Pass some data into the templates
- Create some dummy recipes dictionary called 'recipes' in views.py for some context.
- Define a variable called context within the home function and pass the recipes data into it creating an object;
context = {
    'recipes': recipes
  }
- Pass the context variable into the return render statement.
- Using logic, create and end a loop to go through the 'recipe' object to pull data;
{% for recipe in recipes %}
<h1>{{recipe.title}}</h1>
<p>{{recipe.author}} | {{recipe.date_posted}}</p>
<h5>{{recipe.content}}</h5>
<hr />
{% endfor %}

## Create a Base file for the same content across all of the app pages
- Create a file called base.html in the recipes/templates/recipes file
- Insert boilerplate html into file and in the body insrt block content and endblock tags; 
{% block content %} {% endblock %}
- In home.html file clear out all html, head and body tags and at top add - {% extends "recipes/base.html" %} and add the block content and end block tags.
- All page content goes in between these tags.


# Adding bootstrap 
- Head to the bootstrap website and to the 'get started' section.
- In the intoduction section part 2, copy and paste the link tag and add into the head tags of base.html.
- Copy and paste the JavaScript script tags and add to bottom of the body tags in base.html.


## Setting up admin
In the terminal;
> python manage.py migrate

> python3 manage.py createsuperuser

- Create a username and password. 
- Type /admin on the end of the browser url to access the admin.

## Creating the model
- Create a recipes model in the recipes/models.py file.
- Make the migrations to update the database, in the terminal run:
> python manage.py makemigrations

> python manage.py migrate
- In order to see the model in the admin it has to be registered in recipes/admin.py, add;
'from . import models'
'admin.site.register(models.Recipe)'
- Run the server, head back to ""/admin, login and add some recipes.
- To use this real data in our template, update the recipes/views.py file home view to query the database.



# Sources
Include() function - djangoproject.com/en/1.11/ref/urls/#django.conf.urls.include
Nav Bar - Bootstrap 