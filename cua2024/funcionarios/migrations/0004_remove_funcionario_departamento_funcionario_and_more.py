# Generated by Django 5.1.3 on 2024-11-19 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_alter_funcionario_departamento_funcionario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='departamento_funcionario',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='estado_funcionario',
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='grado_funcionario',
        ),
    ]