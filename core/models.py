from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    autor = models.ForeignKey(get_user_model, verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)


    def __str__(self) -> str:
        return self.titulo
