from django.contrib import admin

from despesa.models import CategoriaDespesa, Despesa, ParcelaDespesa

# Register your models here.

admin.site.register(Despesa)
admin.site.register(ParcelaDespesa)
admin.site.register(CategoriaDespesa)