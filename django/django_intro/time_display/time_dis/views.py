from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%b %d, %Y", gmtime()),
        "date": strftime(" %H:%M %p"),
    }
    return render(request,'index.html', context)