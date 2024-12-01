from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    name = 'Laura'
    author_date = '30/11/2024 às 8:44pm'
    category = {
        'doces': 'Doces',
        'salgado': 'salgado',
        'bebida': 'bebida'
    }
    ingredients = [
        '2 ovos',
        '3 xicaras de leite',
        '4 azeitonas'
    ]
    return render(request, 'pages/home.html', 
        context = {
            'name': name,
            'author_date': author_date,
            'category': category['doces'],
            'ingredients': ingredients
        }, 
        status = 200
    )
