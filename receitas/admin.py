from django.contrib import admin
from receitas.models import Receita, CategoriaReceita
# Register your models here.
admin.site.register(Receita)
admin.site.register(CategoriaReceita)