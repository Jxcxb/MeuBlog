from django.urls import path
from .views import ListarPostsListView, IndexView, DetalhePostView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('listar', ListarPostsListView.as_view(), name='listagem'),
    path('post/<slug:slug>', DetalhePostView.as_view(), name='post'),
]
