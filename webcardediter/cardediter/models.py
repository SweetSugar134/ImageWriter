from django.db import models

from django.contrib.auth.models import User


class Picture(models.Model):
    image = models.ImageField(upload_to='media/userstory/', verbose_name='Картинка')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class PictureTemplate(models.Model):
    image = models.ImageField(upload_to='media/picture_templates/', verbose_name='Шаблон')
