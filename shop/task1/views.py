from django.shortcuts import render
from django.http import HttpResponse
from .forms import (RegisterForm)
from .models import Buyer, Game
# from django.views.generic import TemplateView


def index(request):
    return render(request, 'index.html')


def platform(request):
    title = 'Главная страница'
    context = {
        'title': title
    }
    return render(request, 'platform.html', context)


def games(request):
    title = 'Игры'
    games = Game.objects.all()
    back_url = "/platform"
    context = {
        'title': title,
        'games': games,
        'len_games': len(games),
        'back_url': back_url
    }
    return render(request, 'games.html', context)


def cart(request):
    title = 'Корзина'
    back_url = "/platform"
    context = {
        'title': title,
        'back_url': back_url
    }
    return render(request, 'cart.html', context)


def sign_up_by_html(request):
    info = {'title': 'Регистрация пользователя с помощью HTML-формы'}
    users = []
    for i in Buyer.objects.all():
        users.append(i.name)
    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        password_repeat = request.POST.get('password_repeat')
        age = request.POST.get('age')

        if login not in users and password == password_repeat and int(age) >= 18:
            Buyer.objects.create(name=login, age=age)
            return HttpResponse(f'Приветствуем, {login}')
        else:
            if login in users:
                info['error'] = 'Пользователь уже существует'
            elif password != password_repeat:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18 лет'
    return render(request, 'registration_page.html', context=info)


def sign_up_by_django(request):
    info = {'title': 'Регистрация пользователя с помощью Django-формы'}
    users = []
    for i in Buyer.objects.all():
        users.append(i.name)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['password_repeat']
            age = form.cleaned_data['age']

            if login not in users and password == password_repeat and int(age) >= 18:
                Buyer.objects.create(name=login, age=age)
                return HttpResponse(f'Приветствуем, {login}')
            else:
                if login in users:
                    info['error'] = 'Пользователь уже существует'
                elif password != password_repeat:
                    info['error'] = 'Пароли не совпадают'
                elif int(age) < 18:
                    info['error'] = 'Вы должны быть старше 18 лет'
    else:
        info['form'] = RegisterForm()
    return render(request, 'registration_page.html', context=info)
