from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'tourist/home.html', )

def about(request):
    return render(request, 'tourist/about.html', )

def contact(request):
    return render(request, 'tourist/contact.html', )

def login(request):
    return render(request, 'tourist/login.html', )


