from django import forms
from . models import Despesa,CategoriaDespesa

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = "__all__"

class CategoriaDespesaForm(forms.ModelForm):
    class Meta:
        model = CategoriaDespesa
        fields = "__all__"