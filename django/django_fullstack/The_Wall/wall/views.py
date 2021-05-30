from django.shortcuts import render, HttpResponse, redirect
from .models import *

def welcome(request):
    if "email" not in request.session:
        return redirect('/')
    else:
        context= {
            "posts": Post.objects.all()
        }
        return render(request,"welcome.html",context)

def newpost(request):
    Post.objects.create(post = request.POST['post'], user_id = user.objects.get(id = request.session['user_id']))
    return redirect("/wall")

def newcomment(request,id):
    i = Post.objects.get(id = id)
    Comment.objects.create(comment = request.POST['comment'], user_id = user.objects.get(id = request.session['user_id']), post_id = i)
    return redirect("/wall")