from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

  
from main.models import Recipe
from main.serializers import RecipeSerializer

# Create your views here.

@swagger_auto_schema(methods=['POST'], request_body=RecipeSerializer)
@api_view(['GET', 'POST'])
def recipe_list(request):

    if request.method == 'GET':
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many = True)

        return JsonResponse(serializer.data, safe=False)
    

    elif request.method == 'POST':
        # data = JSONParser.parse(request)
        serializer = RecipeSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)

    
    

    else:
        pass


@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=RecipeSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
def recipe(request, recipe_id):

    try:

        recipe = Recipe.objects.get(id=recipe_id)

    except:
        return JsonResponse({'message': "Recipe Not Found"}, staus = 400)
    
    if request.method == 'GET':
        
        serializer = RecipeSerializer(recipe)

        return JsonResponse(serializer.data, safe=False )
    
    

    elif request.method == 'PUT':
        # data = JSONParser.parse(request)
        serializer = RecipeSerializer(recipe, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return JsonResponse(serializer.data, status = 201)
        
        return JsonResponse(serializer.errors, status = 400)
    
    elif request.method == 'DELETE':

        recipe.delete()

        return JsonResponse(status = 400)

    else:
        pass


# def index(request):

#     return HttpResponse('Hello MAstering Backend')


# @api_view(['GET', 'POST'])
# def recipe(request):

#     if request.method == 'GET':

#         data = {
#             'status': True,
#             'message': 'sign in successful',
#             'status_code': 201,
#         }

#         return Response({'message': 'you got some data', 'data': data})
    
#     else:
#         data = []
#         return Response({'message':'all_recipes', 'data': data})
    



# @api_view(['POST'])
# def add_recipe(request):

#     if request.method == 'POST':

#         name = request.data['name']
#         details = request.data['details']
#         ingredients = request.data['ingredients']
#         tags = request.data['tags']

#         recipe = Recipe.objects.create(name=name, details = details, ingredients = ingredients, tags = tags)
#         recipe.save()

#         data = {
#             'status': True,
#             'message': 'add recipe successfully',
#             'status_code': 201,
#         }


#         return Response({'message': 'you got some data', 'data': data})
    
#     else:
#         data = []
#         return Response({'message':'all_recipes', 'data': data})
    


# @api_view(['GET'])
# def all_recipe(request):

#     if request.method == 'GET':

#         recipes = Recipe.objects.all()
#         final_recipes = []

#         for recipe in recipes:

#             new_obj ={
#                 'id': recipe.id,
#                 'name': recipe.name,
#                 'details': recipe.details,
#                 'ingredients': recipe.ingredients,
#                 'tags': recipe.tags,
#             }

#             final_recipes.append(new_obj)

#         data = {
#             'status': True,
#             'message': 'Success',
#             'status_code': 201,
#             'recipes': final_recipes
#         }


#         return Response({'message': 'you got some data', 'data': data})
    
#     else:
#         data = []
#         return Response({'message':'all_recipes', 'data': data})


# @api_view(['DELETE'])
# def delete_recipe(request, recipe_id):

#     if request.method == 'DELETE':

#         recipe = Recipe.objects.get(id = recipe_id)
#         recipe.delete()

#         data = {
#             'status': True,
#             'message': 'Recipes Deleted successfully',
#             'status_code': 201,
#         }
        
#         return Response({'message': 'you got some data', 'data': data})
    

# @api_view(['POST'])
# def update_recipe(request, recipe_id):

#     recipe = Recipe.objects.get(id = recipe_id)

#     if request.method == 'POST':


#         name = request.data['name']
#         details = request.data['details']
#         ingredients = request.data['ingredients']
#         tags = request.data['tags']

#         recipe.name = name
#         recipe.details = details
#         recipe.ingredients = ingredients
#         recipe.tags = tags

#         recipe.save()

