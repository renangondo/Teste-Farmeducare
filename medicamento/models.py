from django.db import models
from datetime import date
from django.contrib.auth.models import User
from perfis.models import Fazenda

# Create your models here.
class Medicamento(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Medicamento')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade evalidade =m Estoque')
    validade = models.DateField(verbose_name='Data de Validade')
    fazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE, verbose_name='Fazenda')

    def __str__(self):
        return f"{self.nome} - {self.quantidade}"
    
    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
        ordering = ['validade']

class SaidaMedicamento(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, verbose_name='Medicamento')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade Retirada')
    data_saida = models.DateField(auto_now_add=True, verbose_name='Data da Saída')
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Cadastrado Por')

    def __str__(self):
        return f"{self.medicamento.nome} - {self.quantidade} - {self.data_saida}"

    class Meta:
        verbose_name = 'Saída de Medicamento'
        verbose_name_plural = 'Saídas de Medicamentos'
        ordering = ['-data_saida']

class EntradaMedicamento(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE, verbose_name='Medicamento')
    quantidade = models.PositiveIntegerField(verbose_name='Quantidade Adicionada')
    validade = models.DateField(verbose_name='Data de Validade')
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Cadastrado Por')

    def __str__(self):
        return f"{self.medicamento.nome} - {self.quantidade} - {self.validade}"

    class Meta:
        verbose_name = 'Entrada de Medicamento'
        verbose_name_plural = 'Entradas de Medicamentos'
        ordering = ['-validade']