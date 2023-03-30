from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    STATUS_CHOICES = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)  # Formata a URL
    corpo = models.TextField()
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='rascunho')  # Tamanho do maior status
    criado = models.DateTimeField(auto_now_add=True)
    publicado = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts_autor') #Se o autor for excluído, seus posts também serão

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-publicado',) #Ordenamento decrescente

    def __str__(self):
        return self.titulo
