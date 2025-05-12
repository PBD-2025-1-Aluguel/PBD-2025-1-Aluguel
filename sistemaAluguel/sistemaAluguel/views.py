from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class HomeView(TemplateView):
    template_name = 'home.html'

class RegistroView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = '/login/'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)