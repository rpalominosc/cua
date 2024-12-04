from django.forms import ModelForm

from funcionarios.models import Funcionario, Grado, Departamento, Estado

class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        #widgets = {
        #   }

