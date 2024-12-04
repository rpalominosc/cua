from django.contrib import admin

from funcionarios.models import Funcionario,Grado,Departamento,Estado

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Grado)
admin.site.register(Departamento)
admin.site.register(Estado)


