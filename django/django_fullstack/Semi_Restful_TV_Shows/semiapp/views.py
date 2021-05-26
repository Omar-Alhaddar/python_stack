from django.shortcuts import render, HttpResponse, redirect
from .models import *

def omar1(request):
    all_mod = Show.objects.all()
    context ={
        'all_mod': all_mod
        
    }
    return render(request,"abdullah.html",context)

def create(request):
    Show.objects.create(title=request.POST['title'],network=request.POST['network'],reld=request.POST['date'],desc=request.POST['desc'])
    x = Show.objects.last()
    context ={
        'x': x 
    }
    return redirect("/shows/" + str(x.id))


def omar(request):
    x = Show.objects.last()
    context ={
        'x': x 
    }
    return render(request,"omar.html",context)


def show(request,id):
    i = Show.objects.get(id =id)
    context={
        'id':id,
        'i':i,
    }
    return render(request,"abdullah1.html",context)
    
def delete(request,id):
    d = Show.objects.get(id=id)
    d.delete()
    return redirect('/shows')

def edit(request,id):
    context={
        'id':id,
        'all':Show.objects.get(id=id),
    }

    return render(request,"omar1.html",context)

def update(request,id):
    y =id
    c = Show.objects.get(id=id)
    c.title = request.POST['title']
    c.network = request.POST['network']
    c.reld = request.POST['date']
    c.desc = request.POST['desc']
    c.save()
    return redirect(f"/shows/{y}")