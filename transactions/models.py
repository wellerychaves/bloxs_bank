from django.db import models


class Transaction(models.Model):
    idTransacao = models.AutoField(primary_key=True)
    valor = models.IntegerField()
    dataTransacao = models.DateTimeField(auto_now_add=True)
    idConta = models.ForeignKey(
        "accounts.Account", on_delete=models.CASCADE, null=False
    )
