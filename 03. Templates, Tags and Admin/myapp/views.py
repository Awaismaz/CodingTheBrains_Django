from django.shortcuts import render

# Create your views here.

def index(request):
    #Read the Database
    #Creates Context Variable (dict)
    my_dict={'pages':['One','Two','Three','Four'],
             'courses':['Frontend', 'Backend']}
    
    return render(request, 'myapp/index.html', context=my_dict)

def home(request):
    return render(request, 'myapp/home.html')
