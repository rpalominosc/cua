from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from jsonschema import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from funcionarios.forms import FuncionarioForm, CuaFuncionario, CodFuncionario
from funcionarios.models import Funcionario,Grado
from django.forms import modelform_factory, ModelChoiceField,forms
import random, time


# Create your views here.

def pide_cod_func(request):
    return render (request, "funcionarios/name.html")   

def selecciona_funcionario(request):
    return render (request, "funcionarios/modiffunc.html")   


def verificar_codigo_cua(request):
    if request.method == 'POST':
        codigo_form = CuaFuncionario(request.POST)
        if codigo_form.is_valid():
            codigo = codigo_form.cleaned_data['cua_funcionario']
            try:
                registro = Funcionario.objects.get(cua_funcionario=codigo)    
                funcionario_var = get_object_or_404(Funcionario,pk=registro.id)
                return render(request,'funcionarios/detalle.html', {'funcionario':funcionario_var})
            except ObjectDoesNotExist as e:
                print ('saliendo por el else')
                contexto={
                    'codigo_form': codigo_form,
                    'mensaje_error': 'El código no existe en la base de datos.'
                }
                return render(request, 'funcionarios/name.html',contexto )
    else:
        codigo_form = CuaFuncionario()

    return render(request, 'funcionarios/name.html' , {'codigo_form': codigo_form})


def verificar_codigo_func(request):
    if request.method == 'POST':
        codigo_form = CodFuncionario(request.POST)
        if codigo_form.is_valid():
            codigo = codigo_form.cleaned_data['codigo_funcionario']
            try:
                registro = Funcionario.objects.get(codigo_funcionario=codigo)    
                funcionario_var = get_object_or_404(Funcionario,pk=registro.id)
                return render(request,'funcionarios/detalle.html', {'funcionario':funcionario_var})
            except ObjectDoesNotExist as e:
                return render(request, 'funcionarios/name_func.html', {
                    'codigo_form': codigo_form,
                    'mensaje_error': 'El código no existe en la base de datos.'
                })
    else:
        codigo_form = CodFuncionario()

    return render(request, 'funcionarios/name_func.html' , {'codigo_form': codigo_form})


def recupera_codigo_func(request):
    if request.method == 'POST':
        codigo_form = CodFuncionario(request.POST)
        if codigo_form.is_valid():
            codigo = codigo_form.cleaned_data['codigo_funcionario']
            try:
                registro = Funcionario.objects.get(codigo_funcionario=codigo)    
                funcionario_var = get_object_or_404(Funcionario,pk=registro.id)
                #url = 'http://localhost:8000/editar_funcionario/'
                funcionario = funcionario_var.id
                #data = {'codigo_funcionario':'codigo_funcionario'}
                #response = request.post(url, data=data)
                url = '/editar_funcionario/'
                return render (request,url)
            except ObjectDoesNotExist as e:
                return render(request, 'funcionarios/modiffunc.html', {
                    'codigo_form': codigo_form,
                    'mensaje_error': 'El código no existe en la base de datos.'
                })
    else:
        codigo_form = CodFuncionario()

    return render(request, 'funcionarios/modiffunc.html' , {'codigo_form': codigo_form})


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
    print('llegó a detalle_funcionario', request.method, id)
    #funcionario_var = Funcionario.objects.get(pk=id)
    funcionario_var = get_object_or_404(Funcionario,pk=id)
    return render(request,'funcionarios/detalle.html', {'funcionario':funcionario_var})

def cua_funcionario(request,cuafuncionario):
    #funcionario_var = Funcionario.objects.get(pk=id)
    funcionario_var = get_object_or_404(Funcionario,pk=cua_funcionario)
    return render(request,'funcionarios/detalle.html', {'funcionario':funcionario_var})

    FuncionarioForm = modelform_factory(Funcionario,exclude=[])

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
            return redirect('home')
        
    else:
        formaFuncionario = FuncionarioForm()

    return render (request, "funcionarios/nuevo.html",{'formaFuncionario':formaFuncionario})

def editar_funcionario(request, id):
    print('llegó a editar_funcionario', request.method, 'Primera vez')
    funcionario_var = get_object_or_404(Funcionario,pk=id)
    if request.method == "POST":
        print(funcionario_var.codigo_funcionario, "Cua_funcionario->", funcionario_var.cua_funcionario)
        #print(request.POST)
        formaFuncionario = FuncionarioForm(request.POST , instance=funcionario_var)
        print('Cua de nuevo antes de evaluar form', funcionario_var.cua_funcionario)
        print('Funcionario antes de evaluar form', funcionario_var.codigo_funcionario)

        #print(formaFuncionario)
        if formaFuncionario.is_valid():
            formaFuncionario.save()
            return redirect('home')
        else:
            print(formaFuncionario.errors)
    else:
        formaFuncionario = FuncionarioForm(instance=funcionario_var)
    return render (request, "funcionarios/editar.html",{'formaFuncionario':formaFuncionario})
