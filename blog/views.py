from django.shortcuts import render
from .models import Post
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