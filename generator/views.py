from django.shortcuts import render
from django.http import HttpResponse
import random as r

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    
    thepassword = ''
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('~!@#$%^&*()_+=-'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    length = int(request.GET.get('length', 12))
    
    for x in range(length):
        thepassword += r.choice(characters)
    
    return render(request, 'generator/password.html', {'password':thepassword})
