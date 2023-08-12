from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('accounts:login')
    else:
        form = RegistrationForm()
    
    return render (request, 'accounts/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()
            login (request, user)
            return redirect ('matrimony:profile_list')
    else:
        form = AuthenticationForm()
    
    return render (request, 'accounts/login.html', {'form':form})

def logout_view(request):
    logout (request)
    return redirect ('accounts:login')

def delete_view(request):
    request.user.delete()
    messages.success(request, 'Your Account has been deleted Successfully')
    return redirect ('accounts:login')