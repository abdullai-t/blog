from django.urls import path
from.views import index, about, posts

urlpatterns = [
    path('', posts),
    path('home', index),
    path('about', about),
]