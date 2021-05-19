from django.shortcuts import render, HttpResponse
import random
c = random.randint(1, 100) 
def index(request):
    return render(request,"form.html")

def check(request):
    number = int(request.POST['hadeel'])
    print(c)
    
    if number > c:
        return render(request,'greater.html')
    if number < c:
        return render(request,'smaller.html')
    if number == c:
        return render(request,'equal.html')
    return render(request,"form.html")