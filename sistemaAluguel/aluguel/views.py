# pbd-2025-1-aluguel/pbd-2025-1-aluguel/PBD-2025-1-Aluguel-411179ba61017a5167dd2d9db4166d3b432e4cd5/sistemaAluguel/aluguel/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    """
    Renderiza a página inicial.
    """
    return render(request, 'home.html')

@login_required
def dash(request):
    """
    Renderiza o dashboard, acessível apenas para usuários autenticados.
    """
    return render(request, 'dash.html')

def register(request):
    """
    Processa os pedidos de registro de usuário.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Não foi possível realizar o seu cadastro. Verifique as informações abaixo.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    """
    Processa os pedidos de login.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dash')
            else:
                messages.error(request, 'Nome de usuário ou senha inválidos.')
        else:
            messages.error(request, 'Nome de usuário ou senha inválidos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """
    Processa os pedidos de logout.
    """
    logout(request)
    return redirect('home')