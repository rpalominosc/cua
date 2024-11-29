# Generated by Django 5.1.3 on 2024-11-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_remove_funcionario_departamento_funcionario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='departamento_funcionario',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='estado_funcionario',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='grado_funcionario',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='codigo_funcionario',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]