from django.urls import path
from apps.recipes.views import home, my_view


urlpatterns = [
    path('', home),
    path('sobre/', my_view),
]