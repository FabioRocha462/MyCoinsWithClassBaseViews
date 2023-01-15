from django import forms
from crum import get_current_user
from . models import Despesa,CategoriaDespesa
#from ai.middleware.current_user import CurrentUserMiddleware

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = [
            "name",
            "value",
            "typeDespesa",
            "date",
            "categoria",
        ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'categoria' : forms.RadioSelect(attrs={'class': 'form-control', 'type': 'radio'}),
            'typeDespesa' : forms.RadioSelect(attrs={'class': 'form-control', 'type': 'radio'}),
        }



    
    def __init__(self,*args,**kwargs):
        super(DespesaForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        print(get_current_user().username)
        categorias = CategoriaDespesa.objects.filter(user = get_current_user().id)
        #self.fields['categoria'].widget.attrs["disabled"] = False

class CategoriaDespesaForm(forms.ModelForm):
    class Meta:
        model = CategoriaDespesa
        fields = [
            "name",
        ]
        
    def __init__(self,*args,**kwargs):
        super(CategoriaDespesaForm, self).__init__(*args, **kwargs)
        self.initial['user'] = get_current_user()
        self.fields['user'].widget.attrs["disabled"] = True
