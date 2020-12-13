from django.contrib import admin
from django.urls import path
from MyApp import views 

urlpatterns = [

    path('', views.index, name='home'),
    path('webpages/index', views.index, name='home'),
    path('webpages/movies', views.movies, name='movies'),
    path('webpages/webseries', views.webseries, name='webseries'),
    path('webpages/contact', views.contact, name='contact'),
    path('webpages/about', views.about, name='about'),
    path('webpages/profile', views.profile, name='profile'),
    path('webpages/UserProfile', views.UserProfile, name='UserProfile'),
       
]