from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def posts(request):
    return render(request, 'postagens.html')

def sobre(request):
    return render(request, 'sobre.html')

