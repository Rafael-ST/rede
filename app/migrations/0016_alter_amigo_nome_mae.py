# Generated by Django 5.0.6 on 2024-06-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_liderdeequipe_horario_reuniao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amigo',
            name='nome_mae',
            field=models.CharField(max_length=150, null=True, verbose_name='Nome da Mãe'),
        ),
    ]
