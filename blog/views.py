from django.shortcuts import render
from .models import Post, Tag, Writing
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class WritingList(ListView):
    model = Writing
    template_name = 'writings.html'
    context_object_name = 'writings'
    ordering = ['-published_date']


class WritingDetail(DetailView):
    model = Writing
    template_name = 'writing.html'
    context_object_name = 'writing'


class TagDetail(DetailView):
    model = Tag
    template_name = 'tagged_items.html'
    context_object_name = 'tagged'
    
    def get_context_data(self, **kwargs):
        tagged = super().get_context_data(**kwargs)
        name = self.get_object().name
        tagged['post'] = Post.objects.all().filter(name)
        tagged["writing"] = Writing.objects.all().filter(tags__name=self.get_slug_field)
        return tagged