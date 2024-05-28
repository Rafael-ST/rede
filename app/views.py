from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, BairroSerializer, LiderDeEquipeSerializer
from rest_framework import generics
from .permissions import IsSuperUser
from .models import Bairro, LiderDeEquipe
from django.contrib.auth.models import User, Group

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)


class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]


class BairroListView(generics.ListAPIView):
    queryset = Bairro.objects.all()
    serializer_class = BairroSerializer
    permission_classes = [AllowAny]


class LiderDeEquipeCreateView(generics.CreateAPIView):
    queryset = LiderDeEquipe.objects.all()
    serializer_class = LiderDeEquipeSerializer
    permission_classes = [IsSuperUser]

    def perform_create(self, serializer):
        user = User.objects.create_user(
            username=serializer.validated_data['cpf'],
            email=serializer.validated_data['email'],
            password='Tt@123456'
        )

        lider_group, created = Group.objects.get_or_create(name='Lider')
        user.groups.add(lider_group)


        serializer.save(user=user)
