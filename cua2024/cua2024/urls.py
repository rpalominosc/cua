"""
URL configuration for cua2024 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from funcionarios.views import detalle_funcionario, nuevo_funcionario, editar_funcionario, pide_cod_func
from webapp.views import bienvenido,inicio #, contacto, despedirse



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='index'),
    #path('despedida.html', despedirse),
    #path('contacto', contacto),
    path('detalle_funcionario/<int:id>',detalle_funcionario),
    path('nuevo_funcionario', nuevo_funcionario),
    path('editar_funcionario/<int:id>', editar_funcionario),
    path('bienvenido',bienvenido),
    path('codfuncionario',pide_cod_func),


] 
