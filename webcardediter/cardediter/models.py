import os

from django.db import models

from django.contrib.auth.models import User
from django.utils.html import format_html

from webcardediter.settings import BASE_DIR


class PictureTemplate(models.Model):
    image = models.ImageField(upload_to='media/picture_templates/', verbose_name='Шаблон')
    
    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super().delete(*args, **kwargs)


class StoryPicture(models.Model):
    image = models.ImageField(upload_to='media/userstory/', verbose_name='Шаблон')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def delete(self, *args, **kwargs):
        os.remove(self.image.path)
        super().delete(*args, **kwargs)
