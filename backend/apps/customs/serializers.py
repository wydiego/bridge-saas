# apps/customs/serializers.py
from rest_framework import serializers
from .models import DespachoAduanero, DocumentoDespacho, LiquidacionAduanera
from apps.clients.models import Cliente

class ClienteSimpleSerializer(serializers.ModelSerializer):
    """Serializer básico para Cliente"""
    class Meta:
        model = Cliente
        fields = [
            'id', 
            'nit', 
            'razon_social', 
            'nombre_comercial', 
            'email', 
            'telefono',
            'tipo_cliente',
            'estado'
        ]

class DocumentoDespachoSerializer(serializers.ModelSerializer):
    """Serializer para DocumentoDespacho"""
    class Meta:
        model = DocumentoDespacho
        fields = [
            'id',
            'despacho',
            'tipo_documento',
            'numero_documento', 
            'fecha_emision',
            'archivo',
            'observaciones',
            'fecha_carga'
        ]

class LiquidacionAduaneraSerializer(serializers.ModelSerializer):
    """Serializer para LiquidacionAduanera"""
    class Meta:
        model = LiquidacionAduanera
        fields = [
            'id',
            'despacho',
            'gravamen_aduanero',
            'iva',
            'ice', 
            'iehd',
            'total_tributos',
            'pagado',
            'fecha_pago',
            'numero_comprobante_pago'
        ]

class DespachoAduaneroListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listado de despachos"""
    cliente_razon_social = serializers.CharField(source='cliente.razon_social', read_only=True)
    cliente_nit = serializers.CharField(source='cliente.nit', read_only=True)
    
    class Meta:
        model = DespachoAduanero
        fields = [
            'id', 
            'numero_referencia',
            'estado',
            'fecha_creacion',
            'cliente',
            'cliente_razon_social',
            'cliente_nit',
            'tipo_declaracion',
            'aduana_registro',
            'valor_fob',
            'canal_asignado'
        ]

class DespachoAduaneroDetailSerializer(serializers.ModelSerializer):
    """Serializer detallado para un despacho específico"""
    cliente = ClienteSimpleSerializer(read_only=True)
    documentos = DocumentoDespachoSerializer(many=True, read_only=True, source='documentodespacho_set')
    liquidacion = LiquidacionAduaneraSerializer(read_only=True, source='liquidacionaduanera')
    
    class Meta:
        model = DespachoAduanero
        fields = [
            'id',
            'numero_referencia',
            'cliente',
            'tipo_declaracion',
            'descripcion_mercancia',
            'partida_arancelaria',
            'pais_origen',
            'pais_procedencia', 
            'cantidad',
            'unidad_medida',
            'peso_bruto',
            'peso_neto',
            'valor_fob',
            'valor_cif',
            'tipo_cambio',
            'aduana_registro',
            'numero_manifiesto',
            'fecha_llegada',
            'estado',
            'numero_dim',
            'canal_asignado',
            'usuario_creacion',
            'fecha_creacion',
            'fecha_actualizacion',
            'documentos',
            'liquidacion'
        ]

class DashboardStatsSerializer(serializers.Serializer):
    """Serializer para estadísticas del dashboard"""
    total_despachos = serializers.IntegerField()
    despachos_pendientes = serializers.IntegerField()
    despachos_completados = serializers.IntegerField()
    despachos_en_proceso = serializers.IntegerField()
