from django.contrib import admin

from .models import Empregado, Telefone, CPF, Departamento

# Register your models here.


class EmpregadoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": (
                "nome", "idade", "endereco"
            )
        }),

        ("Wage", {
            "fields": (
                "salario", "cpf", "departamento"
            )
        }),

        ("Email", {
            "fields": (
                "email", "foto"   
            )
        }),
    )
    
    list_display = ["id", "nome", "email"]
    list_filter = ["salario", "idade", "departamento"]
    search_fields = ["salario", "departamento__nome"]



admin.site.register(Empregado, EmpregadoAdmin)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)