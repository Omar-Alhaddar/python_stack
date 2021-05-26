from django.urls import path     
from . import views


urlpatterns = [
    path('/', views.omar1),

    path('/new', views.omar),

    path('/create', views.create),

    path('/<int:id>', views.show),

    path('/delete/<int:id>', views.delete),
    
    path('/<int:id>/edit', views.edit),

    path('/update/<int:id>', views.update),
    
]