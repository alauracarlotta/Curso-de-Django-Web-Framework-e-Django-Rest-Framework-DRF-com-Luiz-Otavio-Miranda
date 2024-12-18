from django.urls import path
from apps.recipes import views


urlpatterns = [
    path(
        '',
        views.home,
        name='home'
    ),
    path(
        'search/',
        views.search,
        name='search'
    ),
    path(
        'category/<int:category_id>/',
        views.category,
        name='category'
    ),
    path(
        'recipe/<int:id>/',
        views.recipes,
        name='recipe'
    ),
]
