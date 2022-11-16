## Installing Django and Setting up the app;
- pip3 install 'django<4'
- pip install --upgrade pip
## Create a project;
- django-admin startproject django_recipes .
## Check that the project server is working;
- python3 manage.py runserver
## Create a new app;
- manage.py startapp recipes 

- In 'django_recipes/settings.py' add the app (recipes) to the INSTALLED_APPS dictionary.

## Create first view and url
- In recipes/views.py import 'HttpResponse package' and create a function that allows a view for the user, for example;

- Create a file in recipes folder called urls.py (so we can work primarily from the app folder) and import views.py from the same file, "from . import views"
- Back in urls.py in django_recipes import the package "include" and create another path - "path('', include('recipes.urls'))" and what this is basically saying is when ever anyone goes to my app website "/" anything go to recipes.urls and use those url paths.
- Create a new url path in recipes/urls.py;
urlpatterns = [
    path('', views.home, name="recipes-home"),
]
- Run server to check it is working! - python3 manage.py runserver

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

