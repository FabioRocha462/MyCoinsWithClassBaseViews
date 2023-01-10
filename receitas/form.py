from django import forms

from . models import Receita,CategoriaReceita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ["name","value","typeReceita","date","categoria"]