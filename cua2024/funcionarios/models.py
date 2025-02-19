from django.db import models
from django.core.validators import RegexValidator

validador = RegexValidator("\d-{1}[A-Z]","Debe ingresar un Código valido")
# Create your models here.

class Grado(models.Model):
    codigo_grado = models.IntegerField(unique=True)
    descripcion_grado = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.descripcion_grado}'
    
class Departamento(models.Model):
    codigo_departamento=models.IntegerField(unique=True)
    descripcion_departamento=models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.descripcion_departamento}'
    
class Estado(models.Model):
    codigo_estado=models.IntegerField(unique=True)
    descripcion_estado=models.CharField(max_length=40)
    
    def __str__(self):
        return f'{self.descripcion_estado}'
    
class Funcionario(models.Model):
    codigo_funcionario = models.CharField(max_length=8, unique=True, validators=[validador])
   
    nombre_funcionario = models.CharField(max_length=150)
    cua_funcionario=models.CharField(max_length=7,unique=True)
    grado_funcionario =models.ForeignKey(Grado,default=20,  on_delete=models.SET_DEFAULT)
    departamento_funcionario = models.ForeignKey(Departamento, default=41, on_delete=models.SET_DEFAULT)
    estado_funcionario = models.ForeignKey(Estado, default=4, on_delete=models.SET_DEFAULT)

    def save(self, *args, **kwargs):
        self.nombre_funcionario = (self.nombre_funcionario).upper()
        return super(Funcionario, self).save(*args, **kwargs)
#
    def __str__(self) :
        return f'Funcionario {self.id}:   {self.codigo_funcionario}  {self.nombre_funcionario} {self.cua_funcionario} {self.departamento_funcionario}  {self.grado_funcionario}  {self.estado_funcionario}'

