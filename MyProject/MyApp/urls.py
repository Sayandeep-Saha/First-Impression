from django.contrib import admin
from django.urls import path
from MyApp import views 

urlpatterns = [

    path('', views.index, name='home'),
    path('webpages/index.html', views.index, name='home'),
    path('webpages/movies.html', views.movies, name='movies'),
    path('webpages/webseries.html', views.webseries, name='webseries'),
    path('webpages/contact.html', views.contact, name='contact'),
    path('webpages/about.html', views.about, name='about'),
    
]