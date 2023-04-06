from django.urls import path
from .views import ListarPosts, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('post/<slug:slug>', ListarPosts.as_view(), name='post'),
]
