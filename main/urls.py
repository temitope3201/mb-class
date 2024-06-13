from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    # path('index/', views.index, name='index'),
    # path('recipe/', views.recipe, name='recipe'),
    # path('add-recipe/', views.add_recipe, name='add-recipe'),
    # path('all-recipe/', views.all_recipe, name='all-recipes'),
    # path('delete-recipe/<int:id>/')

    path('recipe-list/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:recipe_id>', views.recipe, name = 'recipe')
]