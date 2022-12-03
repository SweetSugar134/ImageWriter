from .forms import MainForm, StoryForm, TemplateForm, UploadOwnForm
from .models import PictureTemplate, StoryPicture
from .image_handler import resizer

from django.views.generic.edit import CreateView

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.shortcuts import redirect, render


from django.core.files.uploadedfile import SimpleUploadedFile


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
    else:
        context['form'] = MainForm(request.POST)
        context['x'] = request.POST['x']
        context['y'] = request.POST['y']
        user_from_request = request.user
        user_story = StoryPicture.objects.filter(user=user_from_request)
        context['current_image'] = user_story.last().image.url
        print(request.POST)
        return render(request, 'cardediter/index.html', context=context)


def change_template(request):
    context = {}
    context['form'] = TemplateForm()
    if request.method == 'POST':
        print(request.POST)
        if TemplateForm(request.POST).is_valid():
            user_story = StoryPicture.objects.filter(user=request.user)
            user_story.delete()

            inst = PictureTemplate.objects.get(pk=int(request.POST.get('template'))).image.file.read()
            file_data = {'image': SimpleUploadedFile('test.png', inst)}
            story_form = StoryForm({'user': request.user.pk}, file_data)
            story_form.save()

            return redirect('home')
    return render(request, 'cardediter/change_template.html', context=context)


def upload_own_image(request):
    context = {}
    context['form'] = UploadOwnForm()
    if request.method == 'POST':
        story_form = StoryForm({'user': request.user.pk}, request.FILES)
        if story_form.is_valid():
            user_story = StoryPicture.objects.filter(user=request.user)
            user_story.delete()
            story_form.save()
            resizer(request.FILES.get('image'))
            print(request.FILES, request.POST)
            return redirect('home')
        else:
            print(story_form.errors)
    return render(request, 'cardediter/upload_image.html', context=context)

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


