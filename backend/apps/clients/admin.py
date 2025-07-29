from django.contrib import admin
from .models import Cliente, ContactoCliente, EvaluacionCliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = [
        'nit', 'razon_social', 'tipo_cliente', 'ciudad', 
        'estado', 'volumen_operaciones', 'fecha_registro'
    ]
    list_filter = ['tipo_cliente', 'estado', 'ciudad', 'volumen_operaciones']
    search_fields = ['nit', 'razon_social', 'nombre_comercial', 'email']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(ContactoCliente)
class ContactoClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cliente', 'cargo', 'telefono', 'email', 'es_principal']
    list_filter = ['es_principal', 'cargo']
    search_fields = ['nombre', 'cliente__razon_social', 'email']

@admin.register(EvaluacionCliente)
class EvaluacionClienteAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'fecha_evaluacion', 'calificacion', 'puntaje', 'evaluado_por']
    list_filter = ['calificacion', 'fecha_evaluacion']
    search_fields = ['cliente__razon_social', 'evaluado_por']
