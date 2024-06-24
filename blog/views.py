from .models import Post, Tag
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


class TagDetail(DetailView):
    model = Tag
    template_name = 'tagged_items.html'
    context_object_name = 'tagged'
    queryset = Tag.objects.all()
    
    def get_context_data(self, **kwargs):
        tagged = super().get_context_data(**kwargs)
        tagged['post'] = Post.objects.all().filter(tags__slug=self.kwargs.get('slug'))
        tagged["writing"] = Writing.objects.all().filter(tags__slug=self.kwargs.get('slug'))
        return tagged