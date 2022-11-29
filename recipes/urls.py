from django.urls import path
from . import views

urlpatterns = [
     # url path for all recipes
     path('', views.RecipeListView.as_view(), name="recipes-home"),
     # url path for recipe detail
     path('recipe/<int:pk>/', views.recipe_details,
          name="recipes-detail"),
     path('recipe/add_comment/<int:recipe_id>/', views.add_comment,
          name="add_comment"),
     # url path for create recipes
     path('recipe/create/', views.RecipeCreateView.as_view(),
          name="recipes-create"),
     # url path for update recipe
     path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(),
          name="recipes-update"),
     # url path for delete recipe
     path('recipe/<int:pk>/delete/', views.RecipeDeleteView.as_view(),
          name="recipes-delete"),
     # url path for FAQ page
     path('questions/', views.questions, name="recipes-questions"),

]
