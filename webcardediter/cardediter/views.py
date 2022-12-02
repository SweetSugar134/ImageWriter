from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import render
from .forms import MainForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import PictureTemplate, Picture
from django.core.files.images import ImageFile


# def index(request):
#     if not request.user.is_authenticated:
#         return redirect(reverse_lazy('login'))
#     context = {}
#     form = MainForm({'template': 1})

#     if request.method == 'POST':
#         # print(request.POST)
#         form = MainForm(request.POST)

#         context['form'] = form
#         # context['x'] = request.POST['image.x']
#         # context['y'] = request.POST['image.y']

#         return render(request, 'cardediter/index.html', context=context)

#     form.template = 1
#     print(form.has_changed())

    # inst = PictureTemplate.objects.get(pk=1).image.file.read()
    # file_data = {'image': SimpleUploadedFile('test.png', inst)}
    # templateform = PictureTemplateForm({}, file_data)
    # if templateform.is_valid():
    #     templateform.save()
    #     print(123)
    # else:
    #     print(templateform.errors)
    # e = Picture.objects.create()

    # e.user=request.user
    # e.image=PictureTemplate.objects.get(pk=form.template).image

    # e.save()s

    # context['form'] = form
    # return render(request, 'cardediter/index.html', context=context)


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('login'))
    if request.method == 'GET':
        if hasattr(request.user, 'picture'):
            print('user have related class')
        else:
            print('user have not related class')
        return render(request, 'cardediter/index.html')
        # if not request.user.picture


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


