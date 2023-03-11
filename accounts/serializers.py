from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.Serializer):
    idConta = serializers.IntegerField(read_only=True)
    saldo = serializers.IntegerField(default=0)
    limiteSaqueDiario = serializers.IntegerField(default=2000)
    flagAtivo = serializers.BooleanField(default=True)
    tipoConta = serializers.IntegerField(default=0)
    dataCriacao = serializers.DateTimeField(read_only=True)

    # Função que realiza a criação de uma conta
    def create(self, validated_data: dict) -> Account:
        return Account.objects.create(**validated_data)
