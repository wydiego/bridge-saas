from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DespachoAduaneroViewSet, 
    DocumentoDespachoViewSet, 
    LiquidacionAduaneraViewSet
)

router = DefaultRouter()
router.register(r'despachos', DespachoAduaneroViewSet)
router.register(r'documentos-despacho', DocumentoDespachoViewSet)
router.register(r'liquidaciones', LiquidacionAduaneraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
