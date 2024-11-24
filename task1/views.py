from django.shortcuts import render, redirect
from .forms import UserRegister
from django.http import HttpResponse
from .models import Buyer, Game, News, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('post/')

    try:
        page_posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_posts = paginator.page(1)
    except EmptyPage:
        page_posts = paginator.page(paginator.num_pages)

    return render(request, 'first_task/post_list.html', {'posts/': page_posts})


# def registration_view(request):
#
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('register/')
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'first_task/registration_page.html', {'form': form})
def registration_view(request):
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
                messages.success(request, f"Приветствуем, {username}!")
                return redirect('home/')
        else:
            info['error'] = 'Форма заполнена неверно'
    else:
        form = UserRegister()

    info['form'] = form
    return render(request, 'first_task/registration_page.html', info)


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
# def sign_up_by_django(request):
#     info = {}
#
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#
#             if Buyer.objects.filter(name=username).exists():
#                 info['error'] = 'Пользователь уже существует'
#             elif password != repeat_password:
#                 info['error'] = 'Пароли не совпадают'
#             elif age < 18:
#                 info['error'] = 'Вы должны быть старше 18'
#             else:
#                 Buyer.objects.create(
#                     name=username,
#                     password=password,
#                     age=age
#                 )
#                 info['message'] = f"Приветствуем, {username}!"
#                 return render(request, 'first_task/registration_page.html', info)
#         else:
#             info['error'] = 'Форма заполнена неверно'
#     else:
#         form = UserRegister()
#
#     info['form'] = form
#     return render(request, 'first_task/registration_page.html', info)
def sign_up_by_html(request):
    return registration_view(request)
# def sign_up_by_html(request):
#     return sign_up_by_django(request)


def all_articles(request):
    all_posts = News.objects.all()
    return render(request, 'first_task/menu.html', {'articles': all_posts})


def delete_article(request, id):
    post = News.objects.get(id=id)
    post.delete()
    return redirect('first_task/menu.html')


def filter_published_articles(request):
    published_posts = News.objects.filter(created_at__year=2024)
    return render(request, 'first_task/menu.html', {'articles': published_posts})


def filter_admin_articles(request):
    admin_posts = News.objects.filter(created_by__username='admin_username')
    return render(request, 'first_task/menu.html', {'articles': admin_posts})

