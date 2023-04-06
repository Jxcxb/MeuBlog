from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from core.models import Post


class IndexView(ListView):
    context_object_name = 'posts'
    template_name = "blog/index.html"
    queryset = Post.publicados.all()
    paginate_by = 2

class ListarPosts(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(ListarPosts, self).get_context_data(**kwargs)
        queryset = Post.publicados.get(slug=kwargs['slug'])
        context.update({'item':queryset})
        return context

    context_object_name = 'item'
    template_name = "blog/post/detalheposts.html"
