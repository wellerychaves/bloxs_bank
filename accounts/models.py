from django.db import models


class Account(models.Model):
    idConta = models.AutoField(primary_key=True)
    saldo = models.IntegerField(null=False, blank=True, default=0)
    limiteSaqueDiario = models.IntegerField(null=True, blank=True)
    flagAtivo = models.BooleanField(default=True)
    tipoConta = models.IntegerField(default=0)
    dataCriacao = models.DateTimeField(auto_now_add=True, editable=False)

    # idPessoa: tive problemas ao fazer relacionamento entre tabelas.
    # Irei correr atrás da solução na semana seguinte.
