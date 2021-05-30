from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *


def index(request): 
    return render(request,"index.html")

def reglog(request):
    if request.POST['action'] ==  "register":
        errors = user.objects.reg(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:    
            if request.POST['action'] ==  "register":
                if request.POST['pass'] == request.POST['cpass']: 
                    user.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['pass'])
                    request.session['email'] = request.POST['email']
                    request.session['first_name']= request.POST['first_name']
                    request.session['user_id']= user.objects.last().id
                    return redirect("/wall")
                else:
                    return redirect("/")

    if request.POST['action'] ==  "login":
        errors = user.objects.log(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            if request.POST['action'] ==  "login":
                users = user.objects.filter(email=request.POST['Lemail'])
                if users:
                    if users[0].password == request.POST['Lpass']:
                        request.session['email']=users[0].email
                        request.session['first_name']=users[0].first_name
                        request.session['user_id']=users[0].id
                        return redirect("/wall")
                    else:
                        return redirect("/")
                else:
                    return redirect("/")

def logout(request):
    request.session.clear()
    return redirect("/")

