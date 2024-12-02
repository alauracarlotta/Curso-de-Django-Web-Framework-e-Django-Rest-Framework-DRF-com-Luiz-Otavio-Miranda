from django.http import HttpResponse
from django.shortcuts import render
from utils.faker_recipe import make_recipe

def home(request):
    return render(request, 'recipes/pages/home.html', context = {
        'recipes': [make_recipe() for _ in range(10)]
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
