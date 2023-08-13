from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login, authenticate
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
# Create your views here.
import uuid
from django.core.mail import send_mail
from .models import CustomUser
from django.http import HttpResponse, JsonResponse


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_email_verified = False
            user.email_verification_token = str(uuid.uuid4())
            user.save()

            current_site = get_current_site(request)
            subject = "Activate your Account"
            activation_link = f"http://{current_site}/accounts/verify_email/{user.email_verification_token}/"
            message = f'Click the link to activate your account: {activation_link}'
            send_mail(subject,message,'matrimony@gmail.com',[user.email])
            
            return redirect ('accounts:login')
    else:
        form = RegistrationForm()
    
    return render (request, 'accounts/register.html', {'form':form})

def verify_email_view(request, token):
    try:
        user = CustomUser.objects.get(email_verification_token=token)
        if user:
            user.is_email_verified= True
            user.email_verification_token = None
            user.save()
            return redirect ('accounts:login')
    except:
        return HttpResponse ("Activation link is Invalid!")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()

            if user.is_email_verified:
                login (request, user)
                return redirect ('matrimony:profile_list')
    
            else:
                messages.error(request, "Please Verify your Email")
                return redirect ('accounts:login')
    else:
        form = AuthenticationForm()
    
    return render (request, 'accounts/login.html', {'form':form})

def logout_view(request):
    logout (request)
    if request.method == "POST":
        return JsonResponse({'success': True})
    return redirect ('accounts:login')

def delete_view(request):
    request.user.delete()
    messages.success(request, 'Your Account has been deleted Successfully')
    return redirect ('accounts:login')