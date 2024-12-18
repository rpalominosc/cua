# Generated by Django 5.1.3 on 2024-12-03 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0008_departamento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_estado', models.IntegerField(unique=True)),
                ('descripcion_estado', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='estado_funcionario',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='funcionarios.estado'),
        ),
    ]
