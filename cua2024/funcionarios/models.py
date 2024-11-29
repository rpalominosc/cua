from django.db import models

# Create your models here.

class Grado(models.Model):
    codigo_grado = models.IntegerField(unique=True)
    descripcion_grado = models.CharField(max_length=40)

    def __str__(self):
        return f'Grado: {self.codigo_grado} {self.descripcion_grado}'
    
class Funcionario(models.Model):
    codigo_funcionario = models.CharField(max_length=8, unique=True)
    nombre_funcionario = models.CharField(max_length=150)
    departamento_funcionario = models.IntegerField(default=0)
    grado_funcionario =models.ForeignKey(Grado,default=0, on_delete=models.SET_DEFAULT)
    estado_funcionario = models.IntegerField(default=0)

    def __str__(self) :
        return f'Funcionario {self.id}:   {self.codigo_funcionario}  {self.nombre_funcionario}  {self.departamento_funcionario}  {self.grado_funcionario}  {self.estado_funcionario}'

