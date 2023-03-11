from django.db import models


class Person(models.Model):
    idPessoa = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=32, null=False)
    cpf = models.CharField(max_length=14, null=False, unique=True)
    dataNascimento = models.CharField(max_length=10, null=False)
