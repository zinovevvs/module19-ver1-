from django.shortcuts import render, redirect
from .forms import UserRegister
from django.http import HttpResponse
from .models import Buyer, Game
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def registration_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('first_task/registration_page.html')  # Замените на имя вашего URL после входа
    else:
        form = UserCreationForm()

    return render(request, 'first_task/registration_page.html', {'form': form})

def home_view(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'first_task/home.html', context)

def games_view(request):
    games = Game.objects.all()
    return render(request, 'first_task/games.html', context={'pagename': 'Игры', 'games': games})

def cart_view(request):
    return render(request, 'first_task/cart.html', context={'pagename': 'Корзина'})

# users = ["user1", "user2", "Vasya", "truelogin"]
def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(
                    name=username,
                    password=password,
                    age=age
                )
                info['message'] = f"Приветствуем, {username}!"
                return render(request, 'first_task/registration_page.html', info)
        else:
            info['error'] = 'Форма заполнена неверно'
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)

def sign_up_by_html(request):
    return sign_up_by_django(request)

