from django import forms
from app.models import LiderDeEquipe

class LiderDeEquipeForm(forms.ModelForm):
    class Meta:
        model = LiderDeEquipe
        exclude = ["user"]