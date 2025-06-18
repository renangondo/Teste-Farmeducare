from django.db import models
from django.contrib.auth.models import User

from receita.models import ClienteFornecedor, Fazenda

# Create your models here.
class Despesa(models.Model):
    cliente_fornecedor = models.ForeignKey(ClienteFornecedor, on_delete=models.PROTECT, verbose_name='Cliente/Fornecedor')
    categoria = models.ForeignKey('CategoriaDespesa', on_delete=models.PROTECT, verbose_name='Categoria da Despesa')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Total')
    parcelas = models.IntegerField(default=1, verbose_name='Número de Parcelas')
    descricao = models.TextField(verbose_name='Descrição da Despesa')
    imposto_renda = models.BooleanField(default=False, verbose_name='Imposto de Renda [SIM/NÃO]')
    data_despesa = models.DateField(verbose_name='Data da Despesa')
    fazenda_destino = models.ForeignKey(Fazenda, on_delete=models.PROTECT, verbose_name='Fazenda Destino')
    cadastrado_por = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Cadastrado Por')
    cadastrado_em = models.DateField(verbose_name='Cadastrado Em')
    
    
    def __str__(self):
        return (
            f"Data da Despesa: - {self.data_despesa}\n"
            f"Cliente: - {self.cliente_fornecedor}\n"
            f"Fazenda de Destino: - {self.fazenda_destino}\n"
            f"Categoria: - {self.categoria}\n"
            f"Valor Total: - {self.valor_total}\n"
            f"Cadastrado Por: - {self.cadastrado_por}"
        )
    

class ParcelaDespesa(models.Model):
    despesa = models.ForeignKey(Despesa, on_delete=models.PROTECT)
    ordem_parcela = models.IntegerField(verbose_name='Ordem da Parcela')
    valor_parcela = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor da Parcela')
    data_vencimento = models.DateField(verbose_name='Data de Vencimento')


    def __str__(self):
        return(  
            f"Despesa: - {self.despesa}\n"
            f"Ordem Parcela: - {self.ordem_parcela}\n"
            f"Valor da Parcela: - {self.valor_parcela}\n"
            f"Data Vencimento: - {self.data_vencimento}\n"
        )
    


class CategoriaDespesa(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name='Nome da Categoria')
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = 'Categorias'
        ordering = ['nome']


