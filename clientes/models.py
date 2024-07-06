from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    Salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
    

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao + " - " + self.numero
        