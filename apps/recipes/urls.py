from django.urls import path
from apps.recipes.views import home


urlpatterns = [
    path('', home, name = 'home'),
]