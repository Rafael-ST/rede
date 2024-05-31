from django import forms
from app.models import LiderDeEquipe, Amigo

class LiderDeEquipeForm(forms.ModelForm):
    class Meta:
        model = LiderDeEquipe
        exclude = ["user"]


class AmigoForm(forms.ModelForm):
    class Meta:
        model = Amigo
        exclude = ["lider"]