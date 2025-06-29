from django.contrib import admin
from .models import Movimentacao, Parcela, Categoria
# Register your models here.


admin.site.register(Movimentacao)
admin.site.register(Parcela)    
admin.site.register(Categoria)