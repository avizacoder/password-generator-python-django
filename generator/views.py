from django.shortcuts import render
#from django.http import HttpResponse
import random

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):

    characters = list('abcdefghijklmnñopqRSTUvwxyz')
    generator_password = ''
    
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('-().-/*_'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    for x in range(length):
        generator_password += random.choice(characters)

    return render(request, 'password.html', {'password': generator_password})
