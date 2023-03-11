from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404

from .models import Account
from .serializers import AccountSerializer


class AccountsView(APIView):
    # Função que lista informações de uma conta.
    def get(self, request: Request, account_id) -> Response:
        accounts = get_object_or_404(Account, pk=account_id)
        serializer = AccountSerializer(accounts, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    # Função que realiza a criação de uma conta
    def post(self, request: Request) -> Response:
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class AccountBalanceView(APIView):
    # Função para consultar saldo de uma determinada conta
    # ATENÇÃO: Complementar lógica para listar apenas o dono da conta e o saldo.
    def get(self, request, account_id):
        account = get_object_or_404(Account, pk=account_id)
        serializer = AccountSerializer(account)
        print("aaaaaaaaaaaa", serializer.data)
        return Response(serializer.data)

    # Função para sacar ou depositar valor na conta.
    # ATENÇÃO: Complementar lógica para atualizar apenas o valor da conta.
    def patch(self, request, account_id):

        # verificar se a conta está bloqueada ou não
        
        account = get_object_or_404(Account, pk=account_id)
        serializer = AccountSerializer(account, request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save()
        except KeyError:
            return Response(
                {"error": "não foi possível atualizar o saldo da conta"},
                status.HTTP_400_BAD_REQUEST,
            )


class AccountBlockView(APIView):
    def patch(self, request, account_id):
        # Exclusivo para criação de conta
        ...
