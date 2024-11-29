from django.contrib import admin

from funcionarios.models import Funcionario,Grado

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Grado)