from django.shortcuts import render, HttpResponse
from . import models


recipes = [
  {
    'author': 'Henry',
    'title': 'Meatballs',
    'content': 'Combine ingredients, form into balls, brown, then place in oven.',
    'date_posted': 'Nov 15th, 2022'
  },
  {
    'author': 'Henry',
    'title': 'Chicken Cutlets',
    'content': 'Bread chicken, cook on each side for 8 min',
    'date_posted': 'Nov 10th, 2022'
  },
  {
    'author': 'Henry',
    'title': 'Sub',
    'content': 'Combine ingredients.',
    'date_posted': 'Nov 13th, 2022'
  }
]



# Function renders home page and passes in recipes dictionary
def home(request):
    
    recipes = models.Recipe.objects.all()
    context = {
    'recipes': recipes
  }
    return render(request, "recipes/home.html", context)
    

# Function renders about page
def about(request):
    return render(request, "recipes/about.html")
