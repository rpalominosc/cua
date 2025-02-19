from django import forms
from django.forms import ModelForm

from funcionarios.models import Funcionario, Grado, Departamento, Estado

class FuncionarioForm(ModelForm):

    class Meta:
        model = Funcionario
        #fields = ['codigo_funcionario', 'nombre_funcionario', 'grado_funcionario', 'departamento_funcionario', 'estado_funcionario']
        #exclude = ['cua_funcionario']
        fields = '__all__'
        #widgets = {
        #   }

class CuaFuncionario(forms.Form):
    
   cua_funcionario = forms.CharField(label="Codigo CUA", max_length=7, empty_value="99999-9", widget=forms.TextInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'99999-9',
                                    }))

   
class CodFuncionario(forms.Form):
    
   codigo_funcionario = forms.CharField(label="Codigo Funcionario", max_length=8, empty_value="999999-X", widget=forms.TextInput(attrs={
                                        'class':'form-control',
                                        'placeholder':'999999-X',
                                    }))

class FuncionarioFormparagrabar(ModelForm):
    #cua_funcionario = forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Funcionario
        fields = ['codigo_funcionario', 'nombre_funcionario', 'grado_funcionario', 'departamento_funcionario', 'estado_funcionario']
        def __init__(self, *args, **kwargs):
            super(UserEditForm, self).__init__(*args, **kwargs)
            self.fields['cua_funcionario'].disabled = True
        #cua_funcionario = forms.CharField(disabled=True)  # Campo solo lectura
        #widgets = {
        #   }