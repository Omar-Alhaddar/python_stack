from django.urls import path     
from . import views

urlpatterns = [
    path('wall', views.welcome),
    path('newpost', views.newpost),
    path('newcomment/<int:id>', views.newcomment),
]