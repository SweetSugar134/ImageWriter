from django.shortcuts import render
from .forms import MainForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy



def index(request):
    context = {}
    context['form'] = MainForm()
    if request.method == 'POST':
        print(request.POST)
        context['x'] = request.POST.get('x')
        context['y'] = request.POST.get('y')
    return render(request, 'cardediter/index.html', context=context)


class RegistrationUserView(CreateView):
    template_name = 'cardediter/profiles/registration.html'
    success_url = reverse_lazy('home')
    model = User
    form_class = UserCreationForm
    

class LoginUser(LoginView):
    template_name = 'cardediter/profiles/login.html'
    model = User
    next = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['next'] = reverse_lazy('home')
        return data

    def get_success_url(self):
        return reverse_lazy('home')

    
class LogoutUser(LogoutView):
    next_page = reverse_lazy('home')
