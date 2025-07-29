from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone
import os
from apps.clients.models import Cliente
from apps.customs.models import DespachoAduanero

def documento_upload_path(instance, filename):
    """Genera la ruta donde se guardará el archivo"""
    return f'documentos/{instance.cliente.nit}/{instance.tipo_documento}/{filename}'

class TipoDocumento(models.Model):
    """Catálogo de tipos de documentos"""
    
    CATEGORIA_CHOICES = [
        ('comercial', 'Comercial'),
        ('transporte', 'Transporte'),
        ('origen', 'Origen'),
        ('sanitario', 'Sanitario'),
        ('legal', 'Legal'),
        ('financiero', 'Financiero'),
        ('otros', 'Otros'),
    ]
    
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=15, choices=CATEGORIA_CHOICES)
    es_obligatorio = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'documentos_tipo'
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'
        ordering = ['categoria', 'nombre']
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


class Documento(models.Model):
    """Modelo principal para gestión de documentos"""
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('recibido', 'Recibido'),
        ('validado', 'Validado'),
        ('observado', 'Observado'),
        ('rechazado', 'Rechazado'),
        ('archivado', 'Archivado'),
    ]
    
    MEDIO_CHOICES = [
        ('fisico', 'Físico'),
        ('digital', 'Digital'),
        ('ambos', 'Físico y Digital'),
    ]
    
    # Información básica
    numero_documento = models.CharField(max_length=50)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='documentos')
    despacho = models.ForeignKey(
        DespachoAduanero,  
        on_delete=models.CASCADE,
        related_name='documentos_generales',
        null=True,
        blank=True
    )
    
    # Archivo digital
    archivo = models.FileField(
        upload_to=documento_upload_path,
        validators=[FileExtensionValidator(['pdf', 'jpg', 'jpeg', 'png', 'doc', 'docx', 'xls', 'xlsx'])],
        null=True,
        blank=True
    )
    nombre_original = models.CharField(max_length=255, blank=True, null=True)
    tamaño_archivo = models.IntegerField(null=True, blank=True, help_text="Tamaño en bytes")
    hash_archivo = models.CharField(max_length=64, blank=True, null=True, help_text="Hash SHA-256 del archivo")
    
    # Información del documento
    fecha_documento = models.DateField(help_text="Fecha del documento original")
    fecha_vencimiento = models.DateField(null=True, blank=True)
    emisor = models.CharField(max_length=200, help_text="Quien emitió el documento")
    numero_referencia = models.CharField(max_length=100, blank=True, null=True)
    
    # Estado y validación
    estado = models.CharField(max_length=15, choices=ESTADO_CHOICES, default='pendiente')
    medio = models.CharField(max_length=10, choices=MEDIO_CHOICES, default='digital')
    fecha_recepcion = models.DateTimeField(default=timezone.now)
    fecha_validacion = models.DateTimeField(null=True, blank=True)
    validado_por = models.CharField(max_length=100, blank=True, null=True)
    
    # Observaciones
    observaciones = models.TextField(blank=True, null=True)
    observaciones_validacion = models.TextField(blank=True, null=True)
    
    # Metadatos
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'documentos_documento'
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
        ordering = ['-fecha_recepcion']
        unique_together = ['numero_documento', 'tipo_documento', 'cliente']
    
    def __str__(self):
        return f"{self.numero_documento} - {self.tipo_documento.nombre}"
    
    @property
    def esta_vigente(self):
        """Verifica si el documento está vigente"""
        if not self.fecha_vencimiento:
            return True
        return timezone.now().date() <= self.fecha_vencimiento
    
    @property
    def dias_vencimiento(self):
        """Días hasta el vencimiento (negativo si ya venció)"""
        if not self.fecha_vencimiento:
            return None
        delta = self.fecha_vencimiento - timezone.now().date()
        return delta.days
    
    def save(self, *args, **kwargs):
        """Override save para calcular metadatos del archivo"""
        if self.archivo:
            self.nombre_original = self.archivo.name
            if hasattr(self.archivo, 'size'):
                self.tamaño_archivo = self.archivo.size
        super().save(*args, **kwargs)


class VersionDocumento(models.Model):
    """Control de versiones de documentos"""
    
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE, related_name='versiones')
    version = models.IntegerField(default=1)
    archivo = models.FileField(upload_to=documento_upload_path)
    descripcion_cambios = models.TextField(blank=True, null=True)
    fecha_version = models.DateTimeField(default=timezone.now)
    creado_por = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'documentos_version'
        verbose_name = 'Versión Documento'
        verbose_name_plural = 'Versiones Documento'
        unique_together = ['documento', 'version']
        ordering = ['-version']
    
    def __str__(self):
        return f"{self.documento.numero_documento} v{self.version}"


class RegistroDocumento(models.Model):
    """Registro maestro de control de documentos"""
    
    ACCION_CHOICES = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('validacion', 'Validación'),
        ('observacion', 'Observación'),
        ('archivo', 'Archivo'),
    ]
    
    documento = models.ForeignKey(Documento, on_delete=models.CASCADE, related_name='registros')
    fecha_accion = models.DateTimeField(default=timezone.now)
    accion = models.CharField(max_length=15, choices=ACCION_CHOICES)
    usuario = models.CharField(max_length=100)
    descripcion = models.TextField()
    destinatario = models.CharField(max_length=200, blank=True, null=True)
    
    # Para control de salida
    fecha_devolucion_esperada = models.DateTimeField(null=True, blank=True)
    fecha_devolucion_real = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'documentos_registro'
        verbose_name = 'Registro Documento'
        verbose_name_plural = 'Registros Documento'
        ordering = ['-fecha_accion']
    
    def __str__(self):
        return f"{self.accion} - {self.documento.numero_documento} - {self.fecha_accion.strftime('%Y-%m-%d')}"


class ListaMaestra(models.Model):
    """Lista maestra de control de registros de documentos"""
    
    año = models.IntegerField()
    mes = models.IntegerField()
    total_documentos_recibidos = models.IntegerField(default=0)
    total_documentos_validados = models.IntegerField(default=0)
    total_documentos_observados = models.IntegerField(default=0)
    total_documentos_archivados = models.IntegerField(default=0)
    
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    cerrado_por = models.CharField(max_length=100, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'documentos_lista_maestra'
        verbose_name = 'Lista Maestra'
        verbose_name_plural = 'Listas Maestras'
        unique_together = ['año', 'mes']
        ordering = ['-año', '-mes']
    
    def __str__(self):
        return f"Lista Maestra {self.mes:02d}/{self.año}"