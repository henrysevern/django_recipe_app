from django.db import models
from django.contrib.auth.models import User

# Model for recipes
class Recipe(models.Model):
    # Gives the recipe a maximum title character length of 100 characters
    title = models.CharField(max_length=100)

    description = models.TextField()
    
    #if a user is deleted so are all the recipes the user created 
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Returns the recipe object as its title
    def __str__(self):
        return self.title