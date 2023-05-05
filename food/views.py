from django.shortcuts import render, redirect
from .models import Food

# Create your views here.
# redirect function that redirects the user to the `food_list` view.
def default_view(request):
    return render(request, 'home.html')
#a view function(renders a template) that handles the POST request to add a new food item. It creates a new food object with the name and calories provided in the POST request and saves it to the database.
def add_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        calories = request.POST['calories']
        food = Food(name=name, calories=calories)
        food.save()
        return redirect('food_list')
    return render(request, 'add_food.html')
#unction is a view function that displays a list of all the food items in the database.
def food_list(request):
    foods = Food.objects.all()
    total_calories = sum(food.calories for food in foods)
    return render(request, 'food_list.html', {'foods': foods, 'total_calories': total_calories})

#a view function that handles the POST request to remove a specific food item. It deletes the food object
def remove_food(request, food_id):
    food = Food.objects.get(id=food_id)
    food.delete()
    return redirect('food_list')
#a view function that resets the food list
def reset_calories(request):
    Food.objects.all().delete()
    return redirect('food_list')
