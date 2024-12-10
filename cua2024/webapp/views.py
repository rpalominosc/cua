from django.http import HttpResponse
from django.shortcuts import render

from funcionarios.models import Funcionario

# Create your views here.

def bienvenido(request):
    #mensajes = {'msg1':'Valor Mensaje1','msg2':'Mas mensajes en el mismo dict'}
    no_personas_var= Funcionario.objects.count()
    funcionarios_var = Funcionario.objects.all()
    return render(request, 'bienvenido.html', {'no_personas' : no_personas_var, 'funcionarios' : funcionarios_var})

def inicio(request):
    
    return render(request, 'inicio.html')


#def despedirse(request):
#    return HttpResponse ('Despedida desde Django')

#def contacto(request):
#    return HttpResponse ('Contacto cel : 9 9988 7654 - e-mail: donald@acme.com')