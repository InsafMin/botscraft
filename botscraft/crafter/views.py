from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *


def show_category(request, cat_id):
    posts = Crafter.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'crafter/index.html', context=context)


def index(request):
    posts = Crafter.objects.all()
    context = {
        'posts': posts,
        'title': 'Главная страница'
    }

    return render(request, 'crafter/index.html', context=context)


def about(request):
    context = {
        'title': 'О сайте'
    }
    return render(request, 'crafter/about.html', context=context)


def create_bot(request):
    context = {
        'title': 'Создание бота'
    }
    return render(request, 'crafter/create_bot.html', context=context)


def sign_up(request):
    context = {
        'title': 'Регистрация'
    }
    return render(request, 'crafter/sign_up.html', context=context)


def login(request):
    context = {
        'title': 'Авторизация'
    }
    return render(request, 'crafter/login.html', context=context)


def contact(request):
    context = {
        'title': 'Обратная связь'
    }
    return render(request, 'crafter/contact.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_request(request, request_id):
    return HttpResponse(f"Отображение запроса с id = {request_id}")
