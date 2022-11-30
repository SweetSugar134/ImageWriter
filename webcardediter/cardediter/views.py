from django.shortcuts import render
from .forms import MainForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy



def index(request):
    context = {}
    form = MainForm()
    if request.method == 'POST':
        form.template_id = request.POST['template_id']
    context['form'] = form
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

    def get_success_url(self):
        return reverse_lazy('home')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('home')
