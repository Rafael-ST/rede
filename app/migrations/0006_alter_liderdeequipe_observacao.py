# Generated by Django 5.0.6 on 2024-05-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_horario_reuniap_liderdeequipe_horario_reuniao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liderdeequipe',
            name='observacao',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Observação'),
        ),
    ]
