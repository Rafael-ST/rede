# Generated by Django 5.0.6 on 2024-06-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_liderdeequipe_horario_reuniao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liderdeequipe',
            name='horario_reuniao',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Horário da próxima reunião'),
        ),
        migrations.AlterField(
            model_name='liderdeequipe',
            name='local_reuniao',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Local da próxima reunião'),
        ),
        migrations.AlterField(
            model_name='liderdeequipe',
            name='nome',
            field=models.CharField(max_length=250, verbose_name='Nome Completo'),
        ),
        migrations.AlterField(
            model_name='liderdeequipe',
            name='nome_mae',
            field=models.CharField(default='', max_length=150, verbose_name='Nome da Mãe'),
        ),
        migrations.AlterField(
            model_name='liderdeequipe',
            name='proxima_reuniao',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Data da próxima reunião'),
        ),
        migrations.AlterField(
            model_name='liderdeequipe',
            name='reuniao',
            field=models.CharField(blank=True, choices=[('s', 'Sim'), ('n', 'Não')], max_length=10, null=True, verbose_name='Já fez reunião com seus amigos?'),
        ),
    ]
