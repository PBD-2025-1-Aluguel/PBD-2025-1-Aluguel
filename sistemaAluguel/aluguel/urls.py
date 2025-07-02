from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dash/', views.dash, name='dash'),
    path('register/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('cadastrar-empresa/', views.cadastrarEmpresaView, name='cadastrar_empresa'),
    path('cadastrar-produto/', views.cadastrarProduto, name='cadastrar_produto'),
]