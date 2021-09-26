from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def show_age(request, age):
    return HttpResponse("I am %s years old." % age)
