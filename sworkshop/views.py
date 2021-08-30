from django.shortcuts import render
from .models import Price, News


def index(request):
    news_list = News.objects.all()
    return render(request, 'sworkshop/index.html', {'news_list': news_list})


def about(request):
    return render(request, 'sworkshop/about.html')


def contacts(request):
    return render(request, 'sworkshop/contacts.html')


def services(request):
    price_list = Price.objects.all()
    return render(request, 'sworkshop/services.html', {'price_list': price_list})


def pictures(request):
    return render(request, 'sworkshop/pictures.html')
