from django import forms

from . models import Receita,CategoriaReceita

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ["name","value","typeReceita","date","categoria"]

        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoria' : forms.RadioSelect(attrs={'class': 'form-control', 'type': 'radio'}),
            'typeReceita' : forms.RadioSelect(attrs={'class': 'form-control','type': 'radio'}),
        }

    def __init__(self,*args,**kwargs):
        super(ReceitaForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
