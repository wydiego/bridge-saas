from django.contrib import admin
from .models import TipoDocumento, Documento, VersionDocumento, RegistroDocumento, ListaMaestra

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'categoria', 'es_obligatorio', 'activo']
    list_filter = ['categoria', 'es_obligatorio', 'activo']
    search_fields = ['codigo', 'nombre']

@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = [
        'numero_documento', 'tipo_documento', 'cliente', 'estado', 
        'fecha_documento', 'fecha_vencimiento'
    ]
    list_filter = ['tipo_documento', 'estado', 'medio', 'fecha_documento']
    search_fields = ['numero_documento', 'cliente__razon_social', 'emisor']

@admin.register(VersionDocumento)
class VersionDocumentoAdmin(admin.ModelAdmin):
    list_display = ['documento', 'version', 'fecha_version', 'creado_por']

@admin.register(RegistroDocumento) 
class RegistroDocumentoAdmin(admin.ModelAdmin):
    list_display = ['documento', 'fecha_accion', 'accion', 'usuario', 'destinatario']

@admin.register(ListaMaestra)
class ListaMaestraAdmin(admin.ModelAdmin):
    list_display = ['año', 'mes', 'total_documentos_recibidos', 'total_documentos_validados']