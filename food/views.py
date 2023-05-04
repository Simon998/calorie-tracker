from django.shortcuts import render, redirect
from .models import Food

# Create your views here.
def default_view(request):
    return redirect('food_list')

def add_food(request):
    if request.method == 'POST':
        name = request.POST['name']
        calories = request.POST['calories']
        food = Food(name=name, calories=calories)
        food.save()
        return redirect('food_list')
    return render(request, 'add_food.html')

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

def remove_food(request, food_id):
    food = Food.objects.get(id=food_id)
    food.delete()
    return redirect('food_list')

def reset_calories(request):
    Food.objects.all().delete()
    return redirect('food_list')
