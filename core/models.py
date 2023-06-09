from django.contrib.auth.models import User
from django.db import models
from stdimage import StdImageField


class PublicadosManager(models.Manager): #Gerenciador de contexto
    def get_queryset(self):
        return super().get_queryset().filter(status='publicado')


class Post(models.Model):
    objects = models.Manager()
    publicados = PublicadosManager()
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
    imagem = StdImageField("Imagem",  upload_to='posts',
                           variations={'thumb': {
                               'width': 438,
                               'height': 438,
                               'crop':True
                                                }
                                       },
                           blank=True, null=True
                           )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-publicado',) #Ordenamento decrescente. Isso influencia a forma como os registros são armazenados na base de dados (objects.first/.last)

    def __str__(self):
        return self.titulo
