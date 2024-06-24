from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.db.models.signals import pre_save
from django.dispatch import receiver
from core.utils import unique_slug_generator
from blog.models import Tag

class Writing(models.Model):

    type_choices = (
        ('poetry', 'Poetry'),
        ('story', 'Story'),
        ('essay', 'Essay'),
        ('article', 'Article'),
        ('other', 'Other'),
        ('tutorial', 'Tutorial'),
        ('exploration', 'Exploration'),
        ('movie_review', 'Movie Review'),
        ('book_review', 'Book Review'),
    )

    title = models.CharField(max_length=200)
    body = CKEditor5Field('Text', config_name='extends')
    published_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(max_length=200, unique=True, null = True, blank = True)
    type = models.CharField(max_length=200, default='writing', choices=type_choices)
    
    def __str__(self):
        return self.title
    
@receiver(pre_save, sender=Writing)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
