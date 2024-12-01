from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = 'Laura'
    author_date = '30/11/2024 às 8:44pm'
    category = {
        'doces': 'Doces',
        'salgado': 'salgado',
        'bebida': 'bebida'
    }
    ingredients = [
        '2 ovos',
        '3 xicaras de leite',
        '4 azeitonas'
    ]
    return render(request, 'recipes/pages/home.html', 
        context = {
            'name': name,
            'author_date': author_date,
            'category': category['doces'],
            'ingredients': ingredients
        }, 
        status = 200
    )

""" def recipes(request, id):
    id_recipe = 5
    id = id_recipe
    return render(request, f'recipes/pages/{id}.html') """

def recipes(request, id):
    name = 'Laura'
    author_date = '30/11/2024 às 8:44pm'
    category = {
        'doces': 'Doces',
        'salgado': 'salgado',
        'bebida': 'bebida'
    }
    ingredients = [
        '2 ovos',
        '3 xicaras de leite',
        '4 azeitonas'
    ]
    return render(request, 'recipes/pages/recipe-view.html', 
        context = {
            'name': name,
            'author_date': author_date,
            'category': category['doces'],
            'ingredients': ingredients
        }, 
        status = 200
    )