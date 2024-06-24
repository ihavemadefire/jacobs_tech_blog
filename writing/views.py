from .models import Writing
from django.views.generic import ListView, DetailView

class WritingList(ListView):
    model = Writing
    template_name = 'writing.html'
    context_object_name = 'writing'
    ordering = ['-published_date']


class WritingDetail(DetailView):
    model = Writing
    template_name = 'piece.html'
    context_object_name = 'piece'