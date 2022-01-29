from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios', verbose_name='User')
    name = models.CharField('Name', max_length=30)
    description = models.TextField('Description')

    def __str__(self):
        return self.name


class Image(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='images', verbose_name='Portfolio')
    name = models.CharField('Name', max_length=30)
    description = models.TextField('Description')
    picture = models.ImageField('Picture', upload_to='')


class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments', verbose_name='Image')
    text = models.TextField("Comment's text")
