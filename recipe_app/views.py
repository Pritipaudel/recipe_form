from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from recipe_app.models import recipe_form

# Create your views here.
class RecipeFormView(View):
    template_name = "index.html"

    def get(self, request):
        # Render the form template for GET requests
        return render(request, self.template_name)

    def post(self, request):
        # Handle POST requests and save data
        data = request.POST
        files = request.FILES

        Recipe_name = data.get('recipe_name')
        Recipe_description = data.get('recipe_description')
        Recipe_image = files.get('recipe_image')

        # Save the data into the database
        recipe = recipe_form.objects.create(
            recipe_name=Recipe_name,
            recipe_description=Recipe_description,
            recipe_image=Recipe_image
        )

        # Prepare the response data
        response_data = {
            "Recipe_name": recipe.recipe_name,
            "Recipe_description": recipe.recipe_description,
            "Recipe_image": recipe.recipe_image.url if recipe.recipe_image else None
        }

        # Return a JSON response with the saved data
        return JsonResponse(response_data)
