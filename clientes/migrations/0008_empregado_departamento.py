# Generated by Django 5.0.6 on 2024-07-09 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_remove_empregado_departamentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='empregado',
            name='departamento',
            field=models.ManyToManyField(blank=True, null=True, to='clientes.departamento'),
        ),
    ]