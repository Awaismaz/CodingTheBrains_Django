from django.shortcuts import render
from .models import Profile
from .forms import ContactForm

def ProfileListView(request):
    profiles=Profile.objects.all()
    return render (request, 'matrimony/profile_list.html', {'profiles':profiles})

def ProfileDetailView(request, profile_id):
    profile=Profile.objects.get(id=profile_id)
    return render (request, 'matrimony/profile_detail.html', {'profile':profile})

def ProfileDeleteView(request, profile_id):
    profile=Profile.objects.get(id=profile_id)
    profile.delete()
    profiles=Profile.objects.all()
    return render (request, 'matrimony/profile_list.html', {'profiles':profiles})

def ContactView(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            print(f"NAME: {form.cleaned_data['name']}")
            print(f"EMAIL: {form.cleaned_data['email']}")
            print(f"MESSAGE: {form.cleaned_data['message']}")
    else:
        form = ContactForm()
    
    return render (request, 'matrimony/contact.html', {'form':form})