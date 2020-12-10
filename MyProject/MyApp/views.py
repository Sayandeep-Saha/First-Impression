from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,'webpages/index.html')

def movies(request):
    return render(request,'webpages/movies.html')

def webseries(request):
    return render(request,'webpages/webseries.html')

def contact(request):
    return render(request,'webpages/contact.html')

def about(request):
    return render(request,'webpages/about.html')

def profile(request):
    return render(request,'webpages/profile.html')

