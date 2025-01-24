from django.db import models

# Create your models here.
class recipe_form(models.Model):
    recipe_name = models.CharField(max_length=100)  # Name of the recipe
    recipe_description = models.TextField()  # Description of the recipe
    recipe_image = models.ImageField(upload_to='Images')  # Image field with upload directory

    def __str__(self):
        return f"{self.recipe_name}, {self.recipe_description}"  # String representation of the model
