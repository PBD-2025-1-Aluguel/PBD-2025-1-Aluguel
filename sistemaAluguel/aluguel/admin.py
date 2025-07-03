from django.contrib import admin
from .models import Empresa, Produto, Aluguel


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnpj', 'telefone', 'email')
    search_fields = ('nome', 'cnpj')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_diario', 'disponivel', 'locador')
    list_filter = ('disponivel', 'locador')
    search_fields = ('nome',)


@admin.register(Aluguel)
class AluguelAdmin(admin.ModelAdmin):
    list_display = ('produto', 'data_aluguel', 'data_fim', 'valor', 'cliente')
    list_filter = ('data_aluguel', 'data_fim', 'cliente', 'produto')
    search_fields = ('produto','cliente')
    