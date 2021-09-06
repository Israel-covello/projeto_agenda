from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=155)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=55)
    sobrenome = models.CharField(max_length=55, blank=True) # Campo opcional
    telefone = models.CharField(max_length=55)
    email = models.CharField(max_length=155, blank=True) # Campo opcional
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(max_length=5000, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
