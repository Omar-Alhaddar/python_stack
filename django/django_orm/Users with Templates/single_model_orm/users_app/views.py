from django.shortcuts import render, HttpResponse,redirect
from .models import user

def index(request):
    context = {
    "users": user.objects.all()
    }
    return render(request, "index.html", context)

def processes(request):
    user.objects.create(first_name=request.POST['first'],last_name=request.POST['last'],email_address=request.POST['email'],age=request.POST['age'])
    return redirect("/")