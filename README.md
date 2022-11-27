# Recipe cards
> image 
- Recipe cards is a interactive application for your recipes! Store all your favourite recipes in one place for quick and easy access without having to search through countless recipe books! Create, edit and view all your recipes as well as viewing others on the app. Other users can intereact by liking and commenting, some people might even offer you tips to improve on your own recipes!

## Features 
### Home page
The home page includes the recipes that all users have created, displayed as cards in a masonry style for a responive design with easy and pleasant viewing. Each card contains a recipe title, the user who created, the date created, a short description and a "view recipe" link to display more recipe details. If the recipe creator has provided an image, the card will also display for an appealing visual to the home page. This also gives the cards different sizes. Each card also shows the amount of likes the recipe has recieved. The cards are set in a row of 3 on large screens and decrease down to row of 1 on smaller devices.
> image 

#### Navigation
The navigation bar is featured across all the webs url's. With easy functionality it allows the user to easy navigate around the site, Links include Home, About, Create Recipe, Profile links, Register and Log In, as well as Log Out when user us logged in and a frequently asked questions page. The page link is highlighted to show the user the current page. When the site is loaded on a smaller device the naviagtion is neatly compacted into an interactive burger icon menu.  
> image 

#### Footer
The footer bar is featured across all the webs url's. It includes the social media links to allow the user to keep up to date with the app. With links to Facebook, Twitter, Instagram, Youtube and Linkedin are displayed in a line of icons. When a user hovers over the icons they are changed to a light blue colour. The footer bar also included the sites trademark for copyright purposes.
> image 

### Recipe detail page
The recipe detail page is displayed when the user clicks on the view recipe links on the recipe cards. This page displays everything the user needs for the recipe; title, user created and time, description, method, ingredients, all displayed on a larger card. If an image was provided when the recipe was created it will be set as the background with the card overlaying. Nutritional information, preperation time and amount served are also displayed at the top.

The recipe card is set out for easy and appealing viewing for the user with the most important information being the center point and the secondary information being smaller. The nutritional information is inline below the title in green circles almost imitating the nutritional information seen on food packages in supermarkets. The amount serve and the prep time are below in red squares, this is so its the first thing the user sees and can determine wether they have enough time to make the recipe or wether they need to increase the quantity for more serving size.

The card also includes the amount of likes the recipe has recieved with also the ability to like the recipe, as well as a comments box to view other users comments as well as add your own. This allows users to connect and show interest in others recipes as well as offer tips on changes or additions to the recipe. I believe this makes the app much more interactive with other users. When a user comments a pop up meesage will display to show the comment was published successful.

Also included is quick share buttons to share the recipe on social media sites, Included is Facebook, Twitter, Instagram and Google. This is also good to get more traffic on the web as people can see and sign up to view their friends shared recipe. 

If the user owns the recipe and are in the recipe detail view they will see update and delete buttons to edit their recipe. Users that dont own the recipe will not be able to access these buttons.
> image

### Create recipe page
> image 

### Update/Edit recipe page
> image 

### Delete recipe page
> image 

### Sign Up/Register page 
> image 

### Login page 
> image 

### Profile page 
> image 

### FAQ page
> image 

### Exsisting Features

### Features left to impliment


## Testing
- For all testing documentation, Please refer to TESTING.md 

## Unfixed Bugs
- 

## Deployment and setting up

### Installing Django, Gunicorn, libraries and Setting up the app;
- In the terminal type the following to install django other packages and setting up the workspace;
>  pip3 install 'django<4' gunicorn

>  pip install --upgrade pip

- After those packages have downloaded install some supporting libraries;
>  pip3 install dj_database_url psycopg2

- Next install cloudinary libraries
>  pip3 install dj3-cloudinary-storage
#### Create a requirements.txt file
>  pip3 freeze --local > requirements.txt
#### Create a project;
>  django-admin startproject django_recipes .
#### Check that the project server is working;
> python3 manage.py runserver
#### Create a new app;
>  manage.py startapp recipes 

- In 'django_recipes/settings.py' add the app (recipes) to the INSTALLED_APPS dictionary.

#### Create first view and url;
- In recipes/views.py import 'HttpResponse package' and create a function that allows a view for the user, for example;

- Create a file in recipes folder called urls.py (so we can work primarily from the app folder) and import views.py from the same file, "from . import views"
- Back in urls.py in django_recipes import the package "include" and create another path - "path('', include('recipes.urls'))" and what this is basically saying is when ever anyone goes to my app website "/" anything go to recipes.urls and use those url paths.
- Create a new url path in recipes/urls.py;
urlpatterns = [
    path('', views.home, name="recipes-home"),
]
- Run server to check it is working! 
> python3 manage.py runserver

#### Create HTML templates 
- Create a 'templates' folder in 'recipes' folder, create another folder called 'recipes' in 'templates', and then in that, create a file called 'home.html'.
- In views.py add to the 'home' function - "return render(request, "recipes/home.html")" and delete the return of the HttpResponse. 

#### Pass some data into the templates
- Create some dummy recipes dictionary called 'recipes' in views.py for some context.
- Define a variable called context within the home function and pass the recipes data into it creating an object;
context = {
    'recipes': recipes
  }
- Pass the context variable into the return render statement.
- Using logic, create and end a loop to go through the 'recipe' object to pull data;
{% for recipe in recipes %}
{{recipe.title}}
{{recipe.author}} | {{recipe.date_posted}}
{{recipe.content}}
{% endfor %}

#### Create a Base file for the same content across all of the app pages
- Create a file called base.html in the recipes/templates/recipes file
- Insert boilerplate html into file and in the body insrt block content and endblock tags; 
{% block content %} {% endblock %}
- In home.html file clear out all html, head and body tags and at top add - {% extends "recipes/base.html" %} and add the block content and end block tags.
- All page content goes in between these tags.


### Adding bootstrap 
- Head to the bootstrap website and to the 'get started' section.
- In the intoduction section part 2, copy and paste the link tag and add into the head tags of base.html.
- Copy and paste the JavaScript script tags and add to bottom of the body tags in base.html.


### Setting up admin
In the terminal;
> python manage.py migrate

> python3 manage.py createsuperuser

- Create a username and password. 
- Type /admin on the end of the browser url to access the admin.

### Creating the model
- Create a recipes model in the recipes/models.py file.
- Make the migrations to update the database, in the terminal run:
> python manage.py makemigrations

> python manage.py migrate
- In order to see the model in the admin it has to be registered in recipes/admin.py, add;
'from . import models'
'admin.site.register(models.Recipe)'
- Run the server, head back to ""/admin, login and add some recipes.
- To use this real data in our template, update the recipes/views.py file home view to query the database.

## Deployment

### Setting up the database
- Log in to ElephantSQL.com to access your dashboard.
- Click “Create New Instance”.
- Set up your plan.
- Select “Select Region” and select a data center near you then click "Review".
- Check your details are correct and then click “Create instance”.
- Return to the ElephantSQL dashboard and click on the database instance name for this project
- In the URL section, click the copy icon to copy the database URL

### Deloyment to Heroku
- Create new Heroku App.
- Add Database to App Resources located in the Resources Tab.
- Copy DATABASE_URL value and add to key in config vars section.
#### Create new env.py file on top level directory
- In the new env.py file import "os" libary.
- Set the environment variables.
`os.environ["DATABASE_URL"]` = * your Heroku DATABASE_URL Link *
`os.environ["SECRET_KEY"]` = * Make up your own randomSecretKey *
#### Back in Heroku 
- Add your secret key to the config vars section.
- Add the key "PORT" and the value "8000" also.
#### Prepare our environment and settings.py file
- In settings.py add the following to top of file;
`import os`
`import dj_database_url`

`if os.path.isfile("env.py"):`
   `import env`
- Remove the insecure secret key and replace with `os.environ.get('SECRET_KEY')` to link with the variable on Heroku.
- Comment out the old DataBases Section.
- Add the follwing new DATABASES Section to link to the DATATBASE_URL variable on Heroku;
`DATABASES = {`
   `'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))`
`}`
- Save all files and Make Migrations. In the terminal type;
> python3 manage.py migrate

### Connect Cloudinary
- Create a static file in main directory 
#### Create a Cloudinary account 
- Create a cloudinary account to store static and media files https://cloudinary.com/.
-  In cloudinary.com copy the CLOUDINARY_URL from the dashboard.
#### In envy.py
- Add Cloudinary URL to env.py 
`os.environ["CLOUDINARY_URL"]` = *cloudinary url*
#### In Heroku
- Add Cloudinary URL to Heroku Config Vars;
Key = COUDINARY_URL, Value = *cloudinary url*
- Add DIABLED_COLLECTSTATIC to Heroku Config Vars;
Key = DISABLE_COLLECTSTATIC, Value = 1
#### In settings.py
- Add Cloudinary Libraries to installed apps (order is important);
`INSTALLED_APPS = [`
    `…,`
    `'cloudinary_storage',`
    `'django.contrib.staticfiles',`
    `'cloudinary',`
    `…,`
`]`
- Tell Django to use Cloudinary to store media and static files. Under `STATIC_URL = '/static/'` in settings.py add;
`STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'`
`STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]`
`STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')`

`MEDIA_URL = '/media/'`
`DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`
- Add Heroku Hostname to ALLOWED_HOSTS
`ALLOWED_HOSTS = ["h-recipe-cards.herokuapp.com", "localhost"]`
### Main deployment
- Create Procfile on the top level directory.
- In Procfile, add code `web: gunicorn django_recipes.wsgi`.
#### Push for deployment
In the terminal;
> git add . 

> git commit -m “Deployment Commit”

> git push

- Deploy Content manually through Heroku
- Recipes app should be up and running!

### Local Deployment

In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone my repository:

- `git clone https://github.com/henrysevern/django_recipe_app.git`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/henrysevern/django_recipe_app)

# Sources
- Include() function - https://djangoproject.com/en/1.11/ref/urls/#django.conf.urls.include
- Nav Bar - Bootstrap 
- Crispy Forms - https://django-crispy-forms.readthedocs.io/en/latest/index.html
- Masonary style cards - https://getbootstrap.com/docs/5.2/examples/masonry/
