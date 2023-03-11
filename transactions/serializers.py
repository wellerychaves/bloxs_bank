from rest_framework import serializers


class transactionSerializer(serializers.Serializer):
    idConta = serializers.IntegerField()
    idTransacao = serializers.IntegerField(read_only=True)
    valor = serializers.IntegerField()
    dataTransacao = serializers.DateTimeField()
