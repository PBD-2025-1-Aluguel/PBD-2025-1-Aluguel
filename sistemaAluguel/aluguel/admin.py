from django.contrib import admin
from .models import Empresa, Produto


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone', 'email')
    search_fields = ('nome', 'cnpj')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_diario', 'disponivel', 'locador')
    list_filter = ('disponivel', 'locador')
    search_fields = ('nome',)