from django.db import models

# Create your models here.


class Departamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class CPF(models.Model):
    numero = models.CharField(max_length=14)
    data_exp = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.numero


class Empregado(models.Model):
    nome = models.CharField(max_length=100, null=False)
    endereco = models.CharField(max_length=200, blank=False, null=False)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    idade = models.IntegerField()
    email = models.EmailField()
    cpf = models.OneToOneField(CPF, on_delete=models.CASCADE, null=True, blank=True)
    departamento = models.ManyToManyField(Departamento, blank=True)
    foto = models.ImageField(upload_to="cliente_fotos")

    def __str__(self):
        return self.nome
    

class Telefone(models.Model):
    numero = models.CharField(max_length=20)
    descricao = models.CharField(max_length=80)
    empregado = models.ForeignKey(Empregado, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao + " - " + self.numero



