from django import forms
from app.models import LiderDeEquipe, Amigo

class LiderDeEquipeForm(forms.ModelForm):
    class Meta:
        model = LiderDeEquipe
        exclude = ["user"]

        data_nascimento = forms.DateField(input_formats=['%d/%m/%Y'])
        proxima_reuniao = forms.DateField(input_formats=['%d/%m/%Y'])

        # widgets = {
        #     'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        #     'proxima_reuniao': forms.DateInput(attrs={'type': 'date'}),
        # }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bairro'].queryset = self.fields['bairro'].queryset.order_by('nome')


class AmigoForm(forms.ModelForm):
    data_nascimento = forms.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Amigo
        exclude = ["lider"]

    
        # widgets = {
        #         'data_nascimento': forms.DateInput(attrs={'type': 'date'})
        #     }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bairro'].queryset = self.fields['bairro'].queryset.order_by('nome')