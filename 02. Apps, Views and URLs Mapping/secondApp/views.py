from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home1(request):
    #String
    return HttpResponse("Hello World from App2")

def home2(request):
    #html String
    return HttpResponse("<b>This is Home 2 from App2<b>")

def home3(request):
    #html String
    return HttpResponse("<i>This is Home 3 from App2<i>")