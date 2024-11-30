from django.urls import path
from apps.recipes.views import contact, home, about


urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('about/', about),
]