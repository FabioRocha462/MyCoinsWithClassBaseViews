from django.contrib import admin
from despesas.models import Despesa, CategoriaDespesa

# Register your models here.
admin.site.register(Despesa)
admin.site.register(CategoriaDespesa)