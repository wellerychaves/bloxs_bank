from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404

from .models import Person
from .serializers import PersonSerializer
from accounts.serializers import AccountSerializer


class PersonView(APIView):
    def get(self, request: Request, person_id) -> Response:
        person = get_object_or_404(Person, pk=person_id)
        serializer = PersonSerializer(person, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

    # Função que realiza a criação de um usuário
    def post(self, request: Request) -> Response:
        serializer = PersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
