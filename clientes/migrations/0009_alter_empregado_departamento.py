# Generated by Django 5.0.6 on 2024-07-09 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_empregado_departamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empregado',
            name='departamento',
            field=models.ManyToManyField(blank=True, to='clientes.departamento'),
        ),
    ]
