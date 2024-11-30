from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'Laura'
    return render(request, 'pages/home.html', 
        context = {
            'name': name    
        }, 
        status = 200
    )
