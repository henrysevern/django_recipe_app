from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Model for recipes
class Recipe(models.Model):
    # Gives the recipe a maximum title character length of 100 characters
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    ingredients = models.TextField(null=True)
    directions = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    calories = models.CharField(max_length=10, blank=True)
    carbs = models.CharField(max_length=10, blank=True)
    fat = models.CharField(max_length=10, blank=True)
    protein = models.CharField(max_length=10, blank=True)
    time = models.CharField(max_length=10, blank=True)
    servings = models.CharField(max_length=10, blank=True)

    likes = models.ManyToManyField(User, related_name='recipe_likes',
                                   blank=True)

    # When a new instance is made the function tells django where to go
    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={'pk': self.pk})

    # Returns the recipe object as its title
    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
