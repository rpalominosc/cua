from django.shortcuts import render, get_object_or_404, redirect
from jsonschema import ValidationError

from funcionarios.forms import FuncionarioForm
from funcionarios.models import Funcionario,Grado
from django.forms import modelform_factory, ModelChoiceField
import random, time


# Create your views here.

def pide_cod_func(request):
    return render (request, "funcionarios/solicita_codigo.html")    




def valida_existencia_cua():
    existe=True
    while existe:                               # Valida CUA unico  al generarlo
        numero_generado = random.randint(11111,99999)
        digito_generado = random.randint(1,9)
        cua_generado=str(numero_generado)+"-"+str(digito_generado)
        try:
            cua_existe = Funcionario.objects.get(cua_funcionario=cua_generado)
        except Funcionario.DoesNotExist:
            cua_existe = None
            existe=False
    return(cua_generado)

def detalle_funcionario(request,id):
    #funcionario_var = Funcionario.objects.get(pk=id)
    funcionario_var = get_object_or_404(Funcionario,pk=id)
    return render(request,'funcionarios/detalle.html', {'funcionario':funcionario_var})

def cua_funcionario(request,cua_funcionario):
    #funcionario_var = Funcionario.objects.get(pk=id)
    funcionario_var = get_object_or_404(Funcionario,pk=cua_funcionario)
    return render(request,'funcionarios/detalle.html', {'funcionario':funcionario_var})

#FuncionarioForm = modelform_factory(Funcionario,exclude=[])

def nuevo_funcionario(request):
    if request.method == "POST":
        formaFuncionario = FuncionarioForm(request.POST)
        if formaFuncionario.is_valid():
            objeto=formaFuncionario.save(commit=False)
            cua_generado=valida_existencia_cua()
            print(cua_generado)
            objeto.cua_funcionario = cua_generado
        #    formaFuncionario.save()
            objeto.save()
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
