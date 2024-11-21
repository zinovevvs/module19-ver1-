from django.urls import path
from .views import registration_view, sign_up_by_html

urlpatterns = [
    path('', registration_view, name='sign_up'),
    path('registration_view/', sign_up_by_html, name='django_sign_up'),
]
