from django.shortcuts import render, redirect, get_object_or_404

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

from .forms import LiderDeEquipeForm, AmigoForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            return redirect('index')
        if (User.objects.filter(username=email)).exists():
            nome = User.objects.filter(username=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            print(user)
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
    meses = [
        (1, 'Janeiro'),
        (2, 'Fevereiro'),
        (3, 'Março'),
        (4, 'Abril'),
        (5, 'Maio'),
        (6, 'Junho'),
        (7, 'Julho'),
        (8, 'Agosto'),
        (9, 'Setembro'),
        (10, 'Outubro'),
        (11, 'Novembro'),
        (12, 'Dezembro'),
    ]
    bairros = Bairro.objects.all()
    amigos = Amigo.objects.all()
    search = request.POST.get('search')
    bairro = request.POST.get('bairro')
    mes = request.POST.get('mes')
    if mes:
        print(mes)
        amigos = amigos.filter(data_nascimento__month=mes)
    if bairro:
        amigos = amigos.filter(bairro__id__icontains=bairro)
    if search:
        amigos = amigos.filter(nome__icontains=search)
    lider_grupo = False
    if request.user.is_authenticated and request.user.groups.filter(name='Lider').exists():
        lider_grupo = True
        lider = LiderDeEquipe.objects.get(email=request.user.username)
        amigos = Amigo.objects.filter(lider=lider)
    return render(request, 'app/amigos.html', {'amigos':amigos, 'lider_grupo': lider_grupo, 'bairros':bairros, 'meses':meses})


@login_required(login_url="index")
def add_lider(request):
    lider_grupo = False
    if request.user.is_authenticated and request.user.groups.filter(name='Lider').exists():
        lider_grupo = True
        return redirect('amigos')
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
def add_amigo(request):
    if request.method == 'POST':
        form = AmigoForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated and request.user.groups.filter(name='Lider').exists():
                lider = LiderDeEquipe.objects.get(email=request.user.username)
                instance = form.save(commit=False)
                instance.lider = lider
                instance.save()
            form.save()
            messages.success(request, 'Amigo salvo com sucesso')
            form = LiderDeEquipeForm()
        else:
            messages.success(request, 'Verifique o fomulário e tente novamente')
    else:
        form = AmigoForm()

    return render(request, "app/add_amigo.html", {'form': form})


@login_required(login_url="index")
def contatos(request):
    lideres = LiderDeEquipe.objects.all()
    search = request.POST.get('search')
    if search:
        lideres = lideres.filter(nome__icontains=search)
    lider_grupo = False
    if request.user.is_authenticated and request.user.groups.filter(name='Lider').exists():
        lider_grupo = True
        return redirect('amigos')
    return render(request, 'app/contatos.html', {'lideres': lideres, 'lider_grupo': lider_grupo})


@login_required
def excluir_amigo(request, pk):
    instance = get_object_or_404(Amigo, id=pk)
    instance.delete()
    messages.success(request, "Amigo exluido")
    return redirect('amigos')


@login_required
def excluir_lider(request, pk):
    instance = get_object_or_404(LiderDeEquipe, id=pk)
    try:
        user = User.objects.get(username=instance.email)
        user.delete()
        messages.success(request, "Lider de equipe exluido, ele não poderar mais acessar essa rede")
    except:
        messages.success(request, "Esse Lider de equipe não existe ou já pode ter sido excluído")
    return redirect('contatos')


@login_required
def lider_view(request, pk):
    lider = LiderDeEquipe.objects.get(id=pk)
    return render(request, 'app/lider_view.html', {'lider':lider})

