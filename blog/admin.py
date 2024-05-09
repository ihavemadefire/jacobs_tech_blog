from django.contrib import admin
from .models import Post, Tag, Writing

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Writing)