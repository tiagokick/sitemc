from django.db import models
from django.utils import timezone


class Imovel(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=120)
    descricao = models.TextField()
    localizacao = models.TextField()
    tamanho = models.CharField(max_length=80)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
