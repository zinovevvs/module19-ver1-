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
    if request.method == 'POST':
        name = request.POST.get('name')
        balance = request.POST.get('balance', 0)
        age = request.POST.get('age')

        if Buyer.objects.filter(name=name).exists():
            messages.error(request, "Пользователь с таким именем уже существует.")
            return redirect('first_task/games.html')  # Или на тот URL, который нужен

        new_buyer = Buyer.objects.create(
            name=name,
            balance=balance,
            age=age
        )
        messages.success(request, "Пользователь успешно зарегистрирован!")
        return redirect('first_task/games.html')

    return render(request, 'registration_page.html')


def sign_up_by_html(request):
    return sign_up_by_django(request)

