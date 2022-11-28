from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from . import models
from .forms import CommentForm


# Function renders home page and passes in recipes dictionary
def home(request):

    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)


# List view class to view recipes
class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/home.html'
    context_object_name = 'recipes'
    ordering = ['id']


def recipe_details(request, id):
    """
    Function to see a single recipe
    """
    recipe = get_object_or_404(models.Recipe, id=id)
    comments = models.Comment.objects.filter(recipe=recipe, approved=True)
    form = CommentForm(request.POST or None)
    template = "recipes/recipe_detail.html"
    context = {
        "recipe": recipe,
        "comments": comments,
        "form": form,
    }
    return render(request, template, context)


def add_comment(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, id=recipe_id)
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save(commit=False)
            form.instance.recipe = recipe
            form.instance.user = request.user
            form.save()
            messages.success(request, "Your comment is pending approval!")
            return redirect(recipe_details, recipe_id)


# Create view class to create recipes
class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'featured_image', 'directions',
              'ingredients', 'time', 'servings', 'calories', 'carbs',
              'fat', 'protein']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update view class to update recipes
class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description', 'featured_image', 'directions',
              'ingredients', 'time', 'servings', 'calories', 'carbs',
              'fat', 'protein']
    # Function only allows the user to update their own recipes

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Delete view function to delete recipes
class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


# Function renders about page
def about(request):
    return render(request, "recipes/about.html")


# Function renders FAQ page
def questions(request):
    return render(request, "recipes/questions.html")
