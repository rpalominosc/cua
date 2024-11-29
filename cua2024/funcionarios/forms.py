from django.forms import ModelForm

from funcionarios.models import Funcionario

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        widgets = {
            
        }