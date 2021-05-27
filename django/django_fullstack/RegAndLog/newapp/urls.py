from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('reglog', views.reglog),
    path('welcome', views.welcome),
    path('logout', views.logout),
]