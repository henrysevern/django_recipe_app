from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView

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


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe


# Function renders about page
def about(request):
    return render(request, "recipes/about.html")
