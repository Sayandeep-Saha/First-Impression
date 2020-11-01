from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def movies(request):
    return render(request,'movies.html')

def webseries(request):
    return render(request,'webseries.html')

def contact(request):
    return render(request,'contact.html')


