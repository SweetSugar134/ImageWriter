from django.db import models

from django.contrib.auth.models import User
from django.utils.html import format_html

import pathlib

from webcardediter.settings import BASE_DIR


class PictureTemplate(models.Model):
    image = models.ImageField(upload_to='media/picture_templates/', verbose_name='Шаблон')


class StoryPicture(models.Model):
    image = models.ImageField(upload_to='media/userstory/', verbose_name='Шаблон')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def delete(self, *args, **kwargs):
        result_dir = BASE_DIR
        for i in self.picture.url.split('/'): result_dir /= i
        pathlib.Path(result_dir).unlink()
        super().delete(*args, **kwargs)
