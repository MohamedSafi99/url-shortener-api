from django.urls import path
from .views import ShortenURLView, redirect_original

urlpatterns = [
    path('shorten/', ShortenURLView.as_view(), name='shorten-url'),
    path('<str:short_code>/', redirect_original, name='redirect-original'),
]