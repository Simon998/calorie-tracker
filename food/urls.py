from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_view, name='default_view'),
    path('add_food/', views.add_food, name='add_food'),
    path('food_list/', views.food_list, name='food_list'),
    path('remove_food/<int:food_id>/', views.remove_food, name='remove_food'),
    path('reset_calories/', views.reset_calories, name='reset_calories'),
]

