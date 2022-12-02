from .forms import MainForm, StoryForm
from .models import PictureTemplate, StoryPicture

from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.shortcuts import redirect, render


from django.core.files.uploadedfile import SimpleUploadedFile


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
    
    context = {}

    if request.method == 'GET':
        context['form'] = MainForm()
        user_from_request = request.user
        user_story = StoryPicture.objects.filter(user=user_from_request)
        if not user_story:
            inst = PictureTemplate.objects.get(pk=1).image.file.read()
            file_data = {'image': SimpleUploadedFile('test.png', inst)}
            story_form = StoryForm({'user': user_from_request.pk}, file_data)
            story_form.save()
        else:
            context['current_image'] = user_story.last().image.url
        return render(request, 'cardediter/index.html', context=context)
    
    if request.method == 'POST':
        context['form'] = MainForm(request.POST)
        context['x'] = request.POST['x']
        context['y'] = request.POST['y']
        user_from_request = request.user
        user_story = StoryPicture.objects.filter(user=user_from_request)
        context['current_image'] = user_story.last().image.url
        print(request.POST)
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


