from django.shortcuts import render, get_list_or_404, get_object_or_404
from apps.recipes.models import Recipe
from utils.faker_recipe import make_recipe # noqa


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('title')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('id')
    )

    return render(request, 'recipes/pages/categories.html', context={
        'title': recipes[0].category.name,
        'recipes': recipes,
    })


def recipes(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    ingredients = [
        '2 ovos',
        '3 xicaras de leite',
        '4 azeitonas'
    ]
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'title': recipe.title,
        'ingredients': ingredients,
        'is_detail_page': True,
    })
