from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

# Create your views here.

def home1(request):
    #String
    return HttpResponse("Hello World")

def home2(request):
    #html String
    return HttpResponse("<b>This is Home 2<b>")

def home3(request):
    return redirect('/secondApp/3')

def home4(request):
    return redirect('secondApp:home3')

def home5(request):
    my_dict={'Name': 'Awais',
             'Age' : 31}
    return JsonResponse(my_dict)
