from django.urls import path
from apps.recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/category/<int:category_id>/', views.category, name='category'),
    path('recipe/<int:id>/', views.recipes, name='recipe'),
]