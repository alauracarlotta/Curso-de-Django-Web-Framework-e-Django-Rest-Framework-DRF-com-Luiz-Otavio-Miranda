from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("Hello, Django!\n Essa é minha Home, Veja só!!!!")


def my_view(request):
    return HttpResponse("Hello, Django!")
