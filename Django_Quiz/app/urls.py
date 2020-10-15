from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('handleSignup', views.handleSignup, name='handleSignup'),
    path('handleLogin', views.handleLogin, name='handleLogin'),
]