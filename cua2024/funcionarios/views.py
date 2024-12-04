from django.shortcuts import render, get_object_or_404, redirect
from jsonschema import ValidationError

from funcionarios.forms import FuncionarioForm
from funcionarios.models import Funcionario,Grado
from django.forms import modelform_factory, ModelChoiceField


# Create your views here.

def detalle_funcionario(request,id):
    #funcionario_var = Funcionario.objects.get(pk=id)
    funcionario_var = get_object_or_404(Funcionario,pk=id)
    return render(request,'funcionarios/detalle.html', {'funcionario':funcionario_var})

#FuncionarioForm = modelform_factory(Funcionario,exclude=[])

def nuevo_funcionario(request):
    if request.method == "POST":
        formaFuncionario = FuncionarioForm(request.POST)
        if formaFuncionario.is_valid():
            formaFuncionario.save()
            return redirect('index')
        
    else:
        formaFuncionario = FuncionarioForm()

    return render (request, "funcionarios/nuevo.html",{'formaFuncionario':formaFuncionario})

def editar_funcionario(request, id):
    if request.method == "POST":
        funcionario_var = get_object_or_404(Funcionario,pk=id)
        formaFuncionario = FuncionarioForm(request.POST, instance=funcionario_var)
        if formaFuncionario.is_valid():
            formaFuncionario.save()
            return redirect('index')
    else:
        funcionario_var = get_object_or_404(Funcionario,pk=id)
        formaFuncionario = FuncionarioForm(instance=funcionario_var)
   
    return render (request, "funcionarios/editar.html",{'formaFuncionario':formaFuncionario})
