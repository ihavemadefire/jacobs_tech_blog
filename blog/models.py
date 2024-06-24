from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.utils import unique_slug_generator

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null = True, blank = True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null = True, blank = True)
    sub_title = models.CharField(max_length=200)
    body = CKEditor5Field('Text', config_name='extends')
    published_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    

@receiver(pre_save, sender=Post) 
def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance)

@receiver(pre_save, sender=Tag) 
def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 