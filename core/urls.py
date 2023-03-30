from django.urls import path, include
from .views import ListarPostsListView

urlpatterns = [
    path('', ListarPostsListView.as_view(), name='home'),
]
