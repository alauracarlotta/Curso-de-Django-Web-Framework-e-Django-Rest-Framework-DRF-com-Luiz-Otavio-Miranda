from django.urls import path
from apps.recipes.views import home, about


urlpatterns = [
    path('', home),
    path('about/', about),
]