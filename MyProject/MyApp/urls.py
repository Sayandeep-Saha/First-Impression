from django.contrib import admin
from django.urls import path
from MyApp import views 

urlpatterns = [

    path('', views.index, name='home'),
    path('index.html', views.index, name='home'),
    path('movies.html', views.movies, name='movies'),
    path('webseries.html', views.webseries, name='webseries'),
    path('contact.html', views.contact, name='contact'),
    
]