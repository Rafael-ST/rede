# Generated by Django 5.0.6 on 2024-05-31 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_amigo_lider'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='local',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Local de Votação'),
        ),
        migrations.AddField(
            model_name='amigo',
            name='secao',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Seção'),
        ),
        migrations.AddField(
            model_name='amigo',
            name='zona',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Zona'),
        ),
    ]
