# Generated by Django 5.1.3 on 2024-12-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0010_funcionario_cua_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='cua_funcionario',
            field=models.CharField(editable=False, max_length=7, null=True, unique=True),
        ),
    ]