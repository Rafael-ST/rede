from django.db import models
from app.static_data import SIM_NAO
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name="Atualizado em")

    class Meta:
        abstract = True


class Bairro(BaseModel):
    nome = models.CharField(verbose_name='Bairro', max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Bairro'
        verbose_name_plural = 'Bairros'


class LiderDeEquipe(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(verbose_name='Nome', max_length=250)
    apelido = models.CharField(verbose_name='Apelido', max_length=100, null=True, blank=True)
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    cpf = models.CharField(max_length=30, verbose_name='CPF', unique=True)
    nome_mae = models.CharField(max_length=150, verbose_name='Nome da Mãe', null=True, blank=True)
    nome_pai = models.CharField(max_length=150, verbose_name='Nome do Pai', null=True, blank=True)
    ddd = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(99)],
                                      verbose_name='DDD')
    telefone = models.CharField(max_length=20, verbose_name='Telefone') 
    whatsapp = models.CharField(verbose_name='É Whatsapp?', max_length=10, choices=SIM_NAO)
    email = models.CharField(verbose_name='Email', max_length=200, unique=True)
    instagram = models.CharField(verbose_name='Instagram', max_length=50, null=True, blank=True)
    cep = models.CharField(verbose_name='CEP', max_length=10, null=True)
    logradouro = models.CharField(verbose_name='Logradouro', max_length=100, null=True)
    numero = models.PositiveIntegerField(verbose_name='Número', null=True)
    bairro = models.ForeignKey('Bairro', verbose_name="Bairro", on_delete=models.PROTECT, null=True)
    complemento = models.CharField(verbose_name='Complemento', max_length=150, null=True, blank=True)
    candidato = models.CharField(verbose_name='Já foi candidato?', max_length=10, choices=SIM_NAO, null=True)
    cargo = models.CharField(verbose_name='Se sim, qual cargo?', max_length=50, null=True, blank=True)
    ano = models.CharField(verbose_name='Ano de candidatura', max_length=10, null=True, blank=True)
    votos = models.IntegerField(verbose_name='Quantidade de votos', null=True, blank=True)
    comunidades = models.TextField(verbose_name='Principais bairros/comunidade de votos', max_length=1000, null=True)
    reuniao = models.CharField(verbose_name='Já fez reunião com seus amigos?', max_length=10, choices=SIM_NAO, null=True)
    proxima_reuniao = models.DateField(verbose_name='Data da próxima reunião', null=True)
    horario_reuniao = models.TimeField(verbose_name='Horário da próxima reunião', null=True)
    local_reuniao = models.CharField(verbose_name='Local da próxima reunião', max_length=100, null=True)
    observacao = models.TextField(verbose_name='Observação', max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.nome


class Amigo(BaseModel):
    lider = models.ForeignKey('LiderDeEquipe', verbose_name='Lider', on_delete=models.PROTECT)
    nome = models.CharField(verbose_name='Nome Completo', max_length=250)
    apelido = models.CharField(verbose_name='Apelido', max_length=100, null=True, blank=True)
    data_nascimento = models.DateField(verbose_name='Data de nascimento')
    cpf = models.CharField(max_length=30, verbose_name='CPF', unique=True)
    nome_mae = models.CharField(max_length=150, verbose_name='Nome da Mãe', null=True, blank=True)
    nome_pai = models.CharField(max_length=150, verbose_name='Nome do Pai', null=True, blank=True)
    ddd = models.PositiveIntegerField(validators=[MinValueValidator(10), MaxValueValidator(99)],
                                      verbose_name='DDD')
    telefone = models.CharField(max_length=20, verbose_name='Telefone') 
    whatsapp = models.CharField(verbose_name='É Whatsapp?', max_length=10, choices=SIM_NAO)
    email = models.CharField(verbose_name='Email', max_length=200, unique=True, null=True, blank=True)
    instagram = models.CharField(verbose_name='Instagram', max_length=50, null=True, blank=True)
    cep = models.CharField(verbose_name='CEP', max_length=10, null=True)
    logradouro = models.CharField(verbose_name='Logradouro', max_length=100, null=True)
    numero = models.PositiveIntegerField(verbose_name='Número', null=True)
    bairro = models.ForeignKey('Bairro', verbose_name="Bairro", on_delete=models.PROTECT, null=True)
    complemento = models.CharField(verbose_name='Complemento', max_length=150, null=True, blank=True)
    observacao = models.TextField(verbose_name='Observação', max_length=250, null=True, blank=True)