from django.db import models
from django.contrib.auth.models import User


class Empresa(models.Model):
    
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    valor_diario = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    locador = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Aluguel(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_aluguel = models.DateTimeField()
    data_fim = models.DateTimeField()
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.produto