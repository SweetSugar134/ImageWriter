from django.shortcuts import render
from .forms import MainForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('login'))
    context = {}
    if request.method == 'POST':
        print(request.POST)
        form = MainForm(request.POST)
        context['form'] = form
        context['x'] = request.POST['image.x']
        context['y'] = request.POST['image.y']
        return render(request, 'cardediter/index.html', context=context)
    form = MainForm()
    context['form'] = form
    print('here')
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
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class LogoutUser(LogoutView):
    next_page = reverse_lazy('home')
