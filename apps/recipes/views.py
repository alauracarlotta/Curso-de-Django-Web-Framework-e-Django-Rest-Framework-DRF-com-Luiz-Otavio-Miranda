from django.http import HttpResponse
from django.shortcuts import render
from apps.recipes.models import Category, Recipe
from utils.faker_recipe import make_recipe

def home(request):
    # recipes = Recipe.objects.all().order_by('title')
    recipes = Recipe.objects.filter(is_published = True).order_by('title')
    return render(request, 'recipes/pages/home.html', context = {
        'recipes': recipes
    })

""" def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context = {
        'recipes': recipes
    }) """

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id = category_id,
        is_published = True
    ).order_by('-id')
    
    category_name = getattr(recipes.first(), 'category', None)
    return render(request, 'recipes/pages/categories.html', context = {
        'recipes': recipes,
        """ 'title': recipes.first().category.name """
        'title': category_name.name
    })


""" def recipes(request, id):
    id_recipe = 5
    id = id_recipe
    return render(request, f'recipes/pages/{id}.html') """

def recipes(request, id):
    ingredients = [
        '2 ovos',
        '3 xicaras de leite',
        '4 azeitonas'
    ]
    return render(request, 'recipes/pages/recipe-view.html', context = {
        'recipe': make_recipe(),
        'ingredients': ingredients,
        'is_detail_page': True
    })
