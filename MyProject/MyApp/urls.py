from django.contrib import admin
from django.urls import path
from MyApp import views 

urlpatterns = [

    path('', views.index, name='home'),
    path('movies', views.movies, name='movies'),
    path('webseries', views.webseries, name='webseries'),
    
]