from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fazenda(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Fazenda')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Fazendas'
        ordering = ['nome']


class Receita(models.Model):
    cliente_fornecedor = models.ForeignKey('ClienteFornecedor', on_delete=models.PROTECT, verbose_name='Cliente/Fornecedor')
    categoria = models.ForeignKey('Categoria', on_delete=models.PROTECT, verbose_name='Categoria da Receita')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Total')
    parcelas = models.IntegerField(default=1, verbose_name='Número de Parcelas')
    itens_da_receita = models.TextField(verbose_name='Itens da Receita')
    data_receita = models.DateField(verbose_name='Data da Receita')
    fazenda_destino = models.ForeignKey(Fazenda, on_delete=models.PROTECT, verbose_name='Fazenda Destino')
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Cadastrado Por')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')
    documento = models.FileField(upload_to='documentos_receita/', blank=True, null=True, verbose_name='Documento Anexo')
    
    def __str__(self):
        return (
            f"Data da Receita: - {self.data_receita}\n"
            f"Cliente: - {self.cliente_fornecedor}\n"
            f"Fazenda de Destino: - {self.fazenda_destino}\n"
            f"Categoria: - {self.categoria}\n"
            f"Valor Total: - {self.valor_total}\n"
            f"Cadastrado Por: - {self.cadastrado_por}"
        )
    
    
class ParcelaReceita(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.PROTECT)
    ordem_parcela = models.IntegerField(verbose_name='Ordem da Parcela')
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor da Parcela')
    data_vencimento = models.DateField(verbose_name='Data de Vencimento')
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name='Valor Pago')
    status_pagamento = models.CharField(max_length=50, choices=[('Pendente', 'Pendente'), ('Pago', 'Pago')], default='Pendente', verbose_name='Status do Pagamento')

    def __str__(self):
        return(  
            f"Receita: - {self.receita}\n"
            f"Ordem Parcela: - {self.ordem_parcela}\n"
            f"Valor da Parcela: - {self.valor_parcela}\n"
            f"Data Vencimento: - {self.data_vencimento}\n"
            f"Valor Pago: - {self.valor_pago}\n"
            f"Status do Pagamento: - {self.status_pagamento}"
        )
    


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome da Categoria')
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

class ClienteFornecedor(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome do Cliente/Fornecedor')
    telefone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Telefone')
    inf_adicionais = models.TextField(blank=True, null=True, verbose_name='Informações Adicionais')
    email = models.EmailField(blank=True, null=True, verbose_name='E-mail')
    fazenda = models.ForeignKey(Fazenda, on_delete=models.PROTECT, verbose_name='Fazenda Associada')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Clientes/Fornecedores'
        ordering = ['nome']


