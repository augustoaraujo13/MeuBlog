from django.contrib.auth.models import User
from django.db import models


class Postagem(models.Model):

    # Titulo do post.
    titulo = models.CharField(max_length=255)
    # Iamgem que será exibida na posatgem
    imagem = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True)
    # URL do post.
    link = models.SlugField(max_length=255, unique=True)
    # Texto do post.
    conteudo = models.TextField()
    # Autor do post.
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # Adiciona automaticamente data e hora ao post, quando postado.
    criado = models.DateTimeField(auto_now_add=True)
    # Quando haver atualização no post será mostrada.
    atualizado = models.DateTimeField(auto_now=True)

    # Coloca titulo da postagem no setor de adm.
    def __str__(self):
        return self.titulo

    class Meta:
        # Tipo de ordenação
        ordering = ('-criado',)
        # Nome singular
        verbose_name = 'postagem'
        # Nome mo plural
        verbose_name_plural = 'postagens'
        