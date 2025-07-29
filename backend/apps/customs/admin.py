# backend/apps/customs/admin.py
from django.contrib import admin
from .models import DespachoAduanero, LiquidacionAduanera, DocumentoDespacho

class DocumentoDespachoInline(admin.TabularInline):
    model = DocumentoDespacho
    extra = 0
    fields = ['tipo_documento', 'numero_documento', 'fecha_emision', 'archivo']

class LiquidacionInline(admin.StackedInline):
    model = LiquidacionAduanera
    extra = 1
    fields = ['gravamen_aduanero', 'iva', 'ice', 'iehd', 'total_tributos', 'pagado']
    readonly_fields = ['total_tributos']

@admin.register(DespachoAduanero)
class DespachoAduaneroAdmin(admin.ModelAdmin):
    list_display = [
        'numero_referencia', 'cliente', 'tipo_declaracion', 'estado',
        'valor_cif', 'aduana_registro', 'fecha_creacion'
    ]
    list_filter = ['tipo_declaracion', 'estado', 'aduana_registro', 'fecha_creacion']
    search_fields = ['numero_referencia', 'numero_dim', 'cliente__razon_social']
    inlines = [LiquidacionInline, DocumentoDespachoInline]
    readonly_fields = ['numero_referencia', 'fecha_creacion', 'fecha_actualizacion']
    
    fieldsets = (
        ('Información General', {
            'fields': ('numero_referencia', 'cliente', 'tipo_declaracion', 'estado')
        }),
        ('Datos de la Mercancía', {
            'fields': ('descripcion_mercancia', 'partida_arancelaria', 'pais_origen', 
                      'pais_procedencia', 'cantidad', 'unidad_medida', 'peso_bruto', 'peso_neto')
        }),
        ('Valores', {
            'fields': ('valor_fob', 'valor_cif', 'tipo_cambio')
        }),
        ('Datos del Despacho', {
            'fields': ('aduana_registro', 'numero_manifiesto', 'fecha_llegada', 
                      'numero_dim', 'canal_asignado')
        }),
        ('Auditoría', {
            'fields': ('usuario_creacion', 'fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        })
    )

@admin.register(DocumentoDespacho)
class DocumentoDespachoAdmin(admin.ModelAdmin):
    list_display = ['despacho', 'tipo_documento', 'numero_documento', 'fecha_emision', 'fecha_carga']
    list_filter = ['tipo_documento', 'fecha_emision']
    search_fields = ['numero_documento', 'despacho__numero_referencia']

@admin.register(LiquidacionAduanera)
class LiquidacionAduaneroAdmin(admin.ModelAdmin):
    list_display = ['despacho', 'total_tributos', 'pagado', 'fecha_pago']
    list_filter = ['pagado', 'fecha_pago']
    search_fields = ['despacho__numero_referencia', 'numero_comprobante_pago']