# pbd-2025-1-aluguel/pbd-2025-1-aluguel/PBD-2025-1-Aluguel-411179ba61017a5167dd2d9db4166d3b432e4cd5/sistemaAluguel/aluguel/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dash/', views.dash, name='dash'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]