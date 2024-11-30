from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'Laura'
    return render(request, 'recipes/home.html', 
        context = {
            'name': name    
        }, 
        status = 200
    )

def contact(request):
    teste = 'A vida de Laura é Bela!'
    return render(request, 'correct/temp.html',
        context = {
            'foi': teste
        }
    )

def about(request):
    return HttpResponse("Hello, Django!")
