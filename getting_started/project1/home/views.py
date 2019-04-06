from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('<h1 style="color:red;background-color:yellow;text-align:center;">Welcome to home</h1>')

def about(request):
    return HttpResponse('<h1 style="color:blue;background-color:orange;text-align:center;">Welcome to about page</h1>')

def contact(request):
    return HttpResponse('<h1 style="color:blue;background-color:red;text-align:center;">Welcome to contact page</h1>')
