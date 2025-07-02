from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib import admin

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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':  # <-- CORRIGIDO AQUI (parêntese removido)
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    # Esta linha renderiza o login.html com o formulário
    # (seja um formulário em branco ou um com erros de validação)
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    """
    Processa os pedidos de logout.
    """
    logout(request)
    return redirect('home')

from django.shortcuts import render

def home(request):
    return render(
        request,
        'home.html'
    )

def loginView(request):
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
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def dashboardView(request):
    return render(
        request,
        'dash.html'
    )

#def login(request):
#    if request.method == "GET":
#        return render(request, 'login.html')
#    else:
#        username = request.POST.get('user')
#        senha = request.POST.get('password')
#
#        return HttpResponse(username)
    
