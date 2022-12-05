from django import forms

from .models import PictureTemplate, StoryPicture, Buffer

from django.utils.html import format_html


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return format_html('<img src="{}" width="100" alt="">'.format(obj.image.url))


class MainForm(forms.Form):
    text = forms.CharField(initial='Text', widget=forms.Textarea())
    font_size = forms.IntegerField(initial=10)
    color = forms.CharField(max_length=7, initial='#ffffff', widget=forms.TextInput(attrs={'type': 'color'}))
    # image = forms.ImageField(widget=forms.FileInput(attrs={'type': 'image', 'src': 'https://i.pinimg.com/736x/0b/6f/aa/0b6faa695924bb5464ec043782ba6d7f.jpg'}))


class TemplateForm(forms.Form):
    template = MyModelChoiceField(queryset=PictureTemplate.objects.all(), widget=forms.RadioSelect, required=False)


class StoryForm(forms.ModelForm):
    class Meta:
        model = StoryPicture
        fields = '__all__'
    

class UploadOwnForm(forms.Form):
    image = forms.ImageField()


class BufferForm(forms.ModelForm):
    class Meta:
        model = Buffer
        fields = '__all__'
