from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    # API URLs
    path('api/', include([
        path('auth/', include('apps.authentication.urls')),
        path('clients/', include('apps.clients.urls')),
        path('customs/', include('apps.customs.urls')),  # ← ESTA LÍNEA ES IMPORTANTE
        path('documents/', include('apps.documents.urls')),
        path('dashboard/', include('apps.dashboard.urls')),
        path('reports/', include('apps.reports.urls')),
        path('audit/', include('apps.audit.urls')),
    ])),
    # API Documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
