from django.db import models

from django.contrib.auth.models import User
from django.utils.html import format_html


class PictureTemplate(models.Model):
    image = models.ImageField(upload_to='media/picture_templates/', verbose_name='Шаблон')


class StoryPicture(models.Model):
    image = models.ImageField(upload_to='media/userstory/', verbose_name='Шаблон')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
