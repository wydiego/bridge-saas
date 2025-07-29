# apps/customs/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, Count
from .models import DespachoAduanero, DocumentoDespacho, LiquidacionAduanera
from .serializers import (
    DespachoAduaneroListSerializer,
    DespachoAduaneroDetailSerializer,
    DocumentoDespachoSerializer,
    LiquidacionAduaneraSerializer,
    DashboardStatsSerializer
)

class DespachoAduaneroViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar despachos aduaneros
    """
    queryset = DespachoAduanero.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        """Usar diferentes serializers según la acción"""
        if self.action == 'list':
            return DespachoAduaneroListSerializer
        return DespachoAduaneroDetailSerializer
    
    def get_queryset(self):
        """Filtrar despachos por parámetros de consulta"""
        queryset = DespachoAduanero.objects.select_related('cliente')
        
        # Filtros opcionales
        estado = self.request.query_params.get('estado')
        cliente_id = self.request.query_params.get('cliente')
        
        if estado:
            queryset = queryset.filter(estado=estado)
        if cliente_id:
            queryset = queryset.filter(cliente_id=cliente_id)
            
        return queryset.order_by('-fecha_creacion')
    
    @action(detail=False, methods=['get'])
    def dashboard_stats(self, request):
        """
        Endpoint para obtener estadísticas del dashboard
        """
        try:
            # Contar despachos por estado
            total = DespachoAduanero.objects.count()
            pendientes = DespachoAduanero.objects.filter(
                Q(estado='pendiente') | Q(estado='PENDIENTE')
            ).count()
            completados = DespachoAduanero.objects.filter(
                Q(estado='completado') | Q(estado='COMPLETADO')
            ).count()
            en_proceso = DespachoAduanero.objects.filter(
                Q(estado='en_proceso') | Q(estado='EN_PROCESO')
            ).count()
            
            stats_data = {
                'total_despachos': total,
                'despachos_pendientes': pendientes,
                'despachos_completados': completados,
                'despachos_en_proceso': en_proceso
            }
            
            serializer = DashboardStatsSerializer(stats_data)
            return Response(serializer.data)
            
        except Exception as e:
            return Response(
                {'error': f'Error al obtener estadísticas: {str(e)}'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class DocumentoDespachoViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar documentos de despacho
    """
    queryset = DocumentoDespacho.objects.all()
    serializer_class = DocumentoDespachoSerializer
    permission_classes = [IsAuthenticated]

class LiquidacionAduaneraViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar liquidaciones aduaneras
    """
    queryset = LiquidacionAduanera.objects.all()
    serializer_class = LiquidacionAduaneraSerializer
    permission_classes = [IsAuthenticated]
