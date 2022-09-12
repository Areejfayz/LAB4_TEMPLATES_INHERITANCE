import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import random

# Create your views here.
def tody(request : HttpRequest):
    t = datetime.date.today()
    return render(request, 'home/index.html', {"today": t})


def password(request):

    characters = list('0987654321abcdefghijklmnopqrstuvwxyz')
    password = ''
    for x in range(8):
        password += random.choice(characters)
    return render(request, 'home/pas.html', {'pas':password})

def book(request : HttpRequest):
    book = ["java ", "css", "html"]
    return render(request, 'home/book.html', { "book" : book})
