from django.urls import path
from .views import RecipeFormView  # Properly import the view

urlpatterns = [
    path("", RecipeFormView.as_view(), name="recipe-form"),  # Path defined for the form
]
