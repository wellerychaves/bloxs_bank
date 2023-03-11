from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.Serializer):
    idPessoa = serializers.IntegerField(read_only=True)
    nome = serializers.CharField(max_length=32, allow_null=False)
    cpf = serializers.CharField(max_length=14, allow_null=False)
    dataNascimento = serializers.CharField(allow_null=False)

    def create(self, validated_data: dict) -> Person:

        return Person.objects.create(**validated_data)
