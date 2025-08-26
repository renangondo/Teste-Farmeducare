from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Parceiros(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Empresa Parceira')
    telefone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone')
    if_adicionais = models.TextField(blank=True, null=True, verbose_name='Informações Adicionais')
    email = models.EmailField(max_length=254, blank=True, null=True, verbose_name='E-mail')
    
    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = 'Parceiro'
        verbose_name_plural = 'Parceiros'
        ordering = ['nome']


class Fazenda(models.Model):
    usuarios = models.ManyToManyField(
        User,
        verbose_name='Usuário Responsável',
        related_name='fazendas'
    )
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True) 
    
    def __str__(self):
        return f"{self.nome} - {self.cidade}"

    class Meta:
        verbose_name = 'Fazenda'
        verbose_name_plural = 'Fazendas'
        ordering = ['nome']