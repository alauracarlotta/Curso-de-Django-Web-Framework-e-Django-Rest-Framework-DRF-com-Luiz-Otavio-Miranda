from django.http import HttpResponse
from django.http import Http404

from django.shortcuts import render, get_list_or_404, get_object_or_404
from apps.recipes.models import Recipe
from utils.faker_recipe import make_recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('title')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


""" def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context = {
        'recipes': recipes
    }) """


def category(request, category_id):
    """ recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True
    ).order_by('-id') """

    # Gambiarra => Not found com status 200??
    """ category_name = getattr(
        getattr(recipes.first(), 'category', None),
        'name',
        'Not found'
    ) """

    # jeito 1
    # estoura um erro 404 com HttpResponse
    """ if not recipes:
        return HttpResponse(content='Not Found', status=404) """

    # jeito 2
    # estoura um erro 404 com Http404
    """ if not recipes:
        raise Http404('Not Found <3') """

    # jeito 3
    # from django.shortcuts import render, get_list_or_404   => para uma lista
    # from django.shortcuts import render, get_object_or_404 => ou para um unico objeto
    # trecho inicial de 'recipes' comentado e construiremos abaixo.
    # recipes = get_list_or_404(
    #     Recipe,
    #     category__id=category_id,
    #     is_published=True
    # ) => Podemos mandar a queryset completa

    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('id')
    )

    return render(request, 'recipes/pages/categories.html', context={
        'title': recipes[0].category.name,
        'recipes': recipes,
        # 'title': recipes.first().category.name,
        # 'title': category.name
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
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'ingredients': ingredients,
        'is_detail_page': True
    })
