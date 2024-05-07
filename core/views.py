from django.views.generic import TemplateView
from blog.models import Post


class HomePageView(TemplateView):
    template_name = 'home.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        posts = super().get_context_data(**kwargs)
        posts["posts"] = Post.objects.all()[:5]
        return posts