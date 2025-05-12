from django.contrib import admin
from django.urls import path
from sistemaAluguel.views import HomeView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.RegistroView.as_view(), name='register'),
]
