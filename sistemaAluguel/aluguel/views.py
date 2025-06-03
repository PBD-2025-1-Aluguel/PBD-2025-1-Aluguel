from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

def home(request):
    return render(
        request,
        'home.html'
    )

def loginView(request):
    return render(
        request,
        'login.html'
    )

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
    


