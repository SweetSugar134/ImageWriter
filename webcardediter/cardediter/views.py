from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView

from django.core.files.uploadedfile import SimpleUploadedFile

from django.shortcuts import redirect, render

from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from .forms import MainForm, StoryForm, TemplateForm, UploadOwnForm, BufferForm
from .image_handler import resizer, drawer
from .models import PictureTemplate, StoryPicture, Buffer


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('login'))
    print('!!! index() post:', request.POST)
    context = {}
    user_story = StoryPicture.objects.filter(user=request.user)
    if not user_story:
        inst = PictureTemplate.objects.first().image.file.read()
        if not hasattr(request.user, 'buffer'):
            buffer = BufferForm({'user': request.user}, {'image': SimpleUploadedFile('{}.png'.format(request.user), inst)})
            if buffer.is_valid():
                buffer.save()
        file_data = {'image': SimpleUploadedFile('test.png', inst)}
        story_form = StoryForm({'user': request.user.pk}, file_data)
        story_form.save()
    if request.method == 'GET':
        context['x'] = 0
        context['y'] = 0
        context['form'] = MainForm()        
    else:
        context['form'] = MainForm(request.POST)
        context['color'] = request.POST.get('color')
        context['x'] = request.POST['x']
        context['y'] = request.POST['y']

        x, y = int(request.POST.get('x')), int(request.POST.get('y'))
        text = request.POST.get('text')
        font_size = int(request.POST.get('font_size'))
        color = request.POST.get('color')

        inst = drawer(user_story.last().image, text, (x, y), font_size, color)

        change_buffer(inst, request.user)

    context['story'] = user_story
    context['current_image'] = request.user.buffer.image.url
        
    return render(request, 'cardediter/index.html', context=context)


def change_template(request):
    context = {}
    context['form'] = TemplateForm()
    if request.method == 'POST':
        print(request.POST)
        if TemplateForm(request.POST).is_valid():
            user_story = StoryPicture.objects.filter(user=request.user)
            for instance in user_story:
                instance.delete()
            inst = PictureTemplate.objects.get(pk=int(request.POST.get('template'))).image.file.read()
            change_buffer(inst, request.user)
            file_data = {'image': SimpleUploadedFile('test.png', inst)}
            story_form = StoryForm({'user': request.user.pk}, file_data)
            story_form.save()

            return redirect('home')
    return render(request, 'cardediter/change_template.html', context=context)


def upload_own_image(request):
    context = {}
    context['form'] = UploadOwnForm()
    if request.method == 'POST':
        inst = resizer(request.FILES.get('image'))
        file_data = {'image': SimpleUploadedFile('test.png', inst)}
        story_form = StoryForm({'user': request.user.pk}, file_data)
        print(story_form.errors)
        if story_form.is_valid():
            user_story = StoryPicture.objects.filter(user=request.user)
            for instance in user_story:
                instance.delete()
            story_form.save()

            resized_image = resizer(request.FILES.get('image'))
            inst = resized_image
            change_buffer(inst, request.user)
            file_data = {'image': SimpleUploadedFile('test.png', inst)}
            story_form = StoryForm({'user': request.user.pk}, file_data)
            return redirect('home')
        else:
            print(story_form.errors)
    return render(request, 'cardediter/upload_image.html', context=context)


def draw_text(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('login'))
    print('draw text', request.POST)

    x, y = int(request.POST.get('user.x')), int(request.POST.get('user.y'))
    text = request.POST.get('text')
    font_size = 40
    if request.POST.get('font_size'):
        font_size = int(request.POST.get('font_size'))
    color = request.POST.get('color')
    image_bytes = StoryPicture.objects.filter(user=request.user).last().image
    inst = drawer(image_bytes, text, (x, y), font_size, color)
    change_buffer(inst, request.user)
    file_data = {'image': SimpleUploadedFile('test.png', inst)}
    form = StoryForm({'user': request.user}, file_data)

    if form.is_valid():
        form.save()
    else:
        print(form.errors)
    return redirect('home')


def choose_story_template(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('login'))
    inst = StoryPicture.objects.get(pk=int(request.POST.get('story'))).image.read()
    change_buffer(inst, request.user)
    return redirect('home')



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


def change_buffer(image, user):
    buffer = Buffer.objects.get(user=user)
    buffer.image.delete()
    buffer.image = SimpleUploadedFile('{}.png'.format(user), image)
    buffer.save()