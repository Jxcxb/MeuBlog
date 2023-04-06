from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core.models import Post


class IndexView(ListView):
    context_object_name = 'posts'
    template_name = "blog/index.html"
    queryset = Post.publicados.all()
    paginate_by = 2


class ListarPostsListView(ListView):
    context_object_name = 'posts'
    template_name = "blog/listarposts.html"
    queryset = Post.publicados.all()
    paginate_by = 2


class DetalhePostView(DetailView):
    template_name = "blog/post/detalheposts.html"
    context_object_name = 'post'
    queryset = Post.publicados.all()
