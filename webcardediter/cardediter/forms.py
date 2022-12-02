from django import forms
from .models import PictureTemplate
from django.utils.safestring import mark_safe
from django.utils.html import format_html, conditional_escape


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return format_html('<img src="{}" width="100" alt="">'.format(obj.image.url))


class MainForm(forms.Form):
    template = MyModelChoiceField(queryset=PictureTemplate.objects.all(), widget=forms.RadioSelect)
    text = forms.CharField(required=False)
    # image = forms.ImageField(widget=forms.FileInput(attrs={'type': 'image', 'src': 'https://i.pinimg.com/736x/0b/6f/aa/0b6faa695924bb5464ec043782ba6d7f.jpg'}))
