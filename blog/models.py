from django.db import models
from django import forms
from django.contrib.auth.models import User
import os

class Category(models.Model):
    name = models.CharField(max_length=50, unique = True)
    slug = models.SlugField(max_length=200, unique = True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique = True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'





# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank = True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank = True)
    file_upload = models.FileField(upload_to = 'blog/files/%Y/%m/%d/', blank = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, null = True, on_delete=models.SET_NULL)
    
    category = models.ForeignKey(Category, null=True, blank = True, on_delete=models.SET_NULL)

    tags = models.ManyToManyField(Tag,blank = True)

    def __str__(self):
        return f'[{self.pk}]{self.title}::{self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]




class Team(models.Model):
    title = models.CharField(max_length=30,null=True,default='')
    num = models.IntegerField(null=True,default='')
    content = models.TextField(null=True,default='')
    subcontent = models.TextField(null=True,default='')
    created_date = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return f'/blog/team/'



SET_OF_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )


class Feedback(models.Model):
    name = models.CharField(max_length=20,default='')
    op1=models.CharField(choices=SET_OF_CHOICES,max_length=100,default='')
    op2=models.CharField(choices=SET_OF_CHOICES,max_length=100,default='')
    op3=models.TextField(null=True,default='')

    def get_absolute_url(self):
        return f'/blog/feedback/'
