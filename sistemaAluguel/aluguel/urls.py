from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="marcketplaceHome"),
    path('login',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('dash', views.dashboardView, name='dashboard')
    #path('login/', views.login, name="login")
]
