from django.urls import path
from . import views

urlpatterns = [
    # url path for all recipes
    path('', views.RecipeListView.as_view(), name="recipes-home"),
    # url path for recipe detail
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(),
         name="recipes-detail"),
    # url path for create recipes
    path('recipe/create/', views.RecipeCreateView.as_view(),
         name="recipes-create"),
    # url path for update recipe
    path('recipe/<int:pk>/update/', views.RecipeUpdateView.as_view(),
         name="recipes-update"),
    # url path for about page
    path('about/', views.about, name="recipes-about"),
]
