# Generated by Django 5.1.3 on 2024-11-29 20:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0007_alter_grado_codigo_grado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_departamento', models.IntegerField(unique=True)),
                ('descripcion_departamento', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='departamento_funcionario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='funcionarios.departamento'),
        ),
    ]
