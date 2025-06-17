from django.contrib import admin
from .models import Receita, ParcelaReceita, Categoria, Fazenda, ClienteFornecedor
# Register your models here.

admin.site.register(Fazenda)
admin.site.register(Receita)
admin.site.register(ParcelaReceita)
admin.site.register(Categoria)
admin.site.register(ClienteFornecedor)