from django.db import models

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
    codigo_funcionario = models.CharField(max_length=8, unique=True)
    nombre_funcionario = models.CharField(max_length=150)
    grado_funcionario =models.ForeignKey(Grado,default=0,  on_delete=models.SET_DEFAULT)
    departamento_funcionario = models.ForeignKey(Departamento, default=0, on_delete=models.SET_DEFAULT)
    estado_funcionario = models.ForeignKey(Estado, default=0, on_delete=models.SET_DEFAULT)

    def __str__(self) :
        return f'Funcionario {self.id}:   {self.codigo_funcionario}  {self.nombre_funcionario}  {self.departamento_funcionario}  {self.grado_funcionario}  {self.estado_funcionario}'

