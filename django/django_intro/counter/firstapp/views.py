from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'count' in request.session:
        print('key exists!')
        request.session['count'] = request.session['count'] + 1
    else:
        print("key 'key_name' does NOT exist")
        request.session['count'] = 1

    return render(request,"index.html")

def destroy(request):
    del request.session['count']
    return redirect("/")