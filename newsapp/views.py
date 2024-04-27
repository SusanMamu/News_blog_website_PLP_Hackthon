from django.shortcuts import render
import requests

API_KEY = '82bf2f63c4f04ed0a3689958c1de30b2'


def home(request):
    #country= request.GET.get('country')
    category = request.GET.get('category')

    if category:
        url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']


    context = {
        'articles': articles
    }

    return render(request, 'newsapp/home.html', context)
