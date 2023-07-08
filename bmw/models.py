from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Indra(models.Model):
    name=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)

class Magar(models.Model):
    indra=models.ForeignKey(Indra, on_delete=models.PROTECT)
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    photo=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    summary=RichTextField()
    content=RichTextField()    

class Thapa(models.Model):
    title=models.CharField(max_length=250)
    photo=models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    summary=RichTextField()
    content=RichTextField()


class Category(models.Model):
    title=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    photo=models.ImageField(upload_to='phots/%y/%m/%d/', blank=True)
    content=RichTextField()

class Copyright(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250, unique=True)
    photo=models.ImageField(upload_to='photo/%y/%m/%d', blank=True)
    content=RichTextField()


        