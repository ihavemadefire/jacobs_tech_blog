from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date']


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'