from django import forms
from crum import get_current_user
from . models import Despesa,CategoriaDespesa

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = [
            "name",
            "value",
            "typeDespesa",
            "date",
            "categoria",
            "user",
        ]

    
    def __init__(self,*args,**kwargs):
        super(DespesaForm, self).__init__(*args, **kwargs)
        user = get_current_user()
        self.initial['user'] = user
        # self.fields['user'].widget.attrs["disabled"] = True

class CategoriaDespesaForm(forms.ModelForm):
    class Meta:
        model = CategoriaDespesa
        fields = [
            "name",
            "user"
        ]
    def __init__(self,*args,**kwargs):
        super(CategoriaDespesaForm, self).__init__(*args, **kwargs)
        self.initial['user'] = get_current_user()
        self.fields['user'].widget.attrs["disabled"] = True
