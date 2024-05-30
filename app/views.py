from django.shortcuts import render, redirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, BairroSerializer, LiderDeEquipeSerializer, AmigoSerializer
from rest_framework import generics
from .permissions import IsSuperUser, IsLider
from .models import Bairro, LiderDeEquipe, Amigo
from django.contrib.auth.models import User, Group
from django.contrib import messages, auth

from .forms import LiderDeEquipeForm
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            return redirect('index')
        if (User.objects.filter(username=email)).exists():
            nome = User.objects.filter(username=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('contatos')
            else:
                messages.warning(request, 'Usuário e/ou senha inválido(s)')
                return redirect('index')
        else:
            messages.warning(request, 'Usuário e/ou senha inválido(s)')
            return redirect('index')
    else:
        return render(request, 'app/index.html')
    # if request.method == 'POST':
    #     form = LiderDeEquipeForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         user = User.objects.create_user(
    #         username=form.cleaned_data['email'],
    #         email=form.cleaned_data['email'],
    #         password='Tt@123456')
    #         lider_group = Group.objects.get(name='Lider')
    #         lider_group.user_set.add(user)
    #         messages.success(request, 'Usuário criado com sucesso, passe a senha para o novo usuário: Tt@123456')
    #     else:
    #         messages.Warning(request, 'Erro ao salvar, verifique os dados e tente novamente')
                  
    #         return redirect('index')
    # else:
    #     form = LiderDeEquipeForm()
    # return render(request, 'app/index.html', {'form':form})

@login_required(login_url="index")
def incluir_lider(request):
    if request.method == 'POST':
        form = LiderDeEquipeForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.create_user(
            username=form.cleaned_data['email'],
            email=form.cleaned_data['email'],
            password='Tt@123456')
            lider_group = Group.objects.get(name='Lider')
            lider_group.user_set.add(user)
            messages.success(request, 'Usuário criado com sucesso, passe a senha para o novo usuário: Tt@123456')
        else:
            messages.Warning(request, 'Erro ao salvar, verifique os dados e tente novamente')
                  
            return redirect('incluir_lider')
    else:
        form = LiderDeEquipeForm()
    return render(request, 'app/incluir_lider.html', {'form':form})


def logout(request):
    auth.logout(request)
    return redirect('index')


def loginoperador(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            return redirect('loginoperador')
        if (User.objects.filter(username=email)).exists():
            nome = User.objects.filter(username=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            auth.login(request, user)
            return redirect('incluir_lider')
        else:
            print('Teste')
            messages.warning(request, 'Usuário e/ou senha inválido(s)')
            return redirect('loginoperador')
    else:
        return render(request, 'app/loginoperador.html')

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


class LiderListView(generics.ListAPIView):
    queryset = LiderDeEquipe.objects.all()
    serializer_class = LiderDeEquipeSerializer
    permission_classes = [IsSuperUser]


class LiderDeEquipeCreateView(generics.CreateAPIView):
    queryset = LiderDeEquipe.objects.all()
    serializer_class = LiderDeEquipeSerializer
    permission_classes = [IsSuperUser]

    def perform_create(self, serializer):
        user = User.objects.create_user(
            username=serializer.validated_data['email'],
            email=serializer.validated_data['email'],
            password='Tt@123456'
        )

        lider_group, created = Group.objects.get_or_create(name='Lider')
        user.groups.add(lider_group)


        serializer.save(user=user)


class AmigoListViewAll(generics.ListAPIView):
    queryset = Amigo.objects.all()
    serializer_class = AmigoSerializer
    permission_classes = [IsSuperUser]


class AmigoListView(generics.ListAPIView):
    queryset = Amigo.objects.all()
    serializer_class = AmigoSerializer
    permission_classes = [IsSuperUser | IsLider]

    def get_queryset(self):
        user = self.request.user
        try:
            lider = LiderDeEquipe.objects.get(user=user)
            return Amigo.objects.filter(lider=lider)
        except LiderDeEquipe.DoesNotExist:
            return Amigo.objects.none()


@login_required(login_url="index")
def amigos_lider(request, pk):
    print(pk)
    amigos = Amigo.objects.filter(lider=pk)
    print(amigos)
    return render(request, 'app/amigos_lider.html', {'amigos':amigos})


@login_required(login_url="index")
def amigos(request):
    amigos = Amigo.objects.all()
    return render(request, 'app/amigos.html', {'amigos':amigos})


@login_required(login_url="index")
def add_lider(request):
    if request.method == 'POST':
        form = LiderDeEquipeForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.create_user(
            username=form.cleaned_data['email'],
            email=form.cleaned_data['email'],
            password='Tt@123456')
            lider_group = Group.objects.get(name='Lider')
            lider_group.user_set.add(user)
            messages.success(request, 'Usuário criado com sucesso, passe a senha para o novo usuário: Tt@123456')
            form = LiderDeEquipeForm()
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    print(f"Erro no campo {field}: {error}")

            messages.warning(request, 'Erro ao salvar, verifique os dados e tente novamente')
                  
            return redirect('add_lider')
    else:
        form = LiderDeEquipeForm()
    return render(request, 'app/add_lider.html', {'form':form})


@login_required(login_url="index")
def contatos(request):
    lideres = LiderDeEquipe.objects.all()
    print(lideres)
    contactList = [
    {
        "id": '1',
        "nome": 'Davi',
        "apelido": 'davilte'
    },
    {
        "id": '2',
        "nome": 'Rafael',
        "apelido": 'rafa'
    },
    {
        "id": '3',
        "nome": 'Eurico',
        "apelido": 'professor'
    },
    {
        "id": '4',
        "nome": 'Davi',
        "apelido": 'davilte'
    },
    {
        "id": '5',
        "nome": 'Rafael',
        "apelido": 'rafa'
    },
    {
        "id": '6',
        "nome": 'Eurico',
        "apelido": 'professor'
    },
    {
        "id": '7',
        "nome": 'Davi',
        "apelido": 'davilte'
    },
    {
        "id": '8',
        "nome": 'Rafael',
        "apelido": 'rafa'
    },
    {
        "id": '9',
        "nome": 'Eurico',
        "apelido": 'professor'
    }
    ]
    return render(request, 'app/contatos.html', {"contacts": contactList, 'lideres': lideres})