from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('reglog', views.reglog),
    path('logout', views.logout),
]