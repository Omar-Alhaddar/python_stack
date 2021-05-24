from django.shortcuts import render, HttpResponse, redirect
from .models import user

def index(request): 
    return render(request,"index.html")

def reglog(request):
    if request.POST['action'] ==  "register":
        if request.POST['pass'] == request.POST['cpass']:
            request.session['email'] = request.POST['email']
            user.objects.create(first_name=request.POST['first'],last_name=request.POST['last'],email=request.POST['email'],password=request.POST['pass'])
            return redirect("/welcome")
        else:
            return redirect("/")
    
    if request.POST['action'] ==  "login":
        users = user.objects.filter(email=request.POST['Lemail'])
        if users:
            if users[0].password == request.POST['Lpass']:
                request.session['email']=users[0].email
                return redirect("/welcome")
            return redirect("/")

def welcome(request):
    context={
        "email": request.session['email']
    }
    return render(request,"welcome.html",context)

def logout(request):
    del request.session['email']
    return redirect("/")