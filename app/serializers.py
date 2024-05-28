from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Bairro, LiderDeEquipe, Amigo

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class BairroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bairro
        fields = '__all__'


class LiderDeEquipeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    bairro = serializers.PrimaryKeyRelatedField(queryset=Bairro.objects.all())
    bairro = serializers.CharField(source='bairro.nome', read_only=True)
    class Meta:
        model = LiderDeEquipe
        fields = '__all__'



class AmigoSerializer(serializers.ModelSerializer):
    bairro = serializers.PrimaryKeyRelatedField(queryset=Bairro.objects.all())
    bairro = serializers.CharField(source='bairro.nome', read_only=True)
    lider = serializers.PrimaryKeyRelatedField(queryset=LiderDeEquipe.objects.all())
    lider = serializers.CharField(source='lider.nome', read_only=True)

    class Meta:
        model = Amigo
        fields = '__all__'