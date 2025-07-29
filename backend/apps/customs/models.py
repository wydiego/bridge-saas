# backend/apps/customs/models.py
from django.db import models
from django.contrib.auth import get_user_model
from apps.clients.models import Cliente

User = get_user_model()

class DespachoAduanero(models.Model):
    # Tipos de declaración según tu información
    TIPO_DECLARACION_CHOICES = [
        ('IM4', 'Importación para el Consumo'),
        ('EX1', 'Exportación Definitiva'),
        ('IM5', 'Admisión Temporal'),
        ('EX3', 'Reexportación'),
        ('IT1', 'Importación Temporal'),
        ('ET1', 'Exportación Temporal'),
    ]
    
    ESTADO_CHOICES = [
        ('BORRADOR', 'Borrador - En preparación'),
        ('ELABORADO', 'Elaborado - Listo para enviar'),
        ('ENVIADO', 'Enviado - Transmitido a SIDUNEA'),
        ('OBSERVADO', 'Observado - Con observaciones'),
        ('PAGADO', 'Pagado - Tributos cancelados'),
        ('NUMERADO', 'Numerado - DIM/DUI asignado'),
        ('EN_AFORO', 'En Aforo - Revisión física/documental'),
        ('LEVANTE', 'Levante - Autorizado para retiro'),
        ('CONCLUIDO', 'Concluido - Mercancía retirada'),
        ('ARCHIVADO', 'Archivado - Proceso finalizado'),
    ]
    
    CANAL_CHOICES = [
        ('VERDE', 'Canal Verde - Levante automático'),
        ('AMARILLO', 'Canal Amarillo - Revisión documental'),
        ('ROJO', 'Canal Rojo - Revisión física'),
    ]
    
    # Identificación
    numero_referencia = models.CharField(
        max_length=50, 
        unique=True,
        verbose_name='Número de Referencia Interno'
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    tipo_declaracion = models.CharField(
        max_length=3, 
        choices=TIPO_DECLARACION_CHOICES
    )
    
    # Datos de la mercancía
    descripcion_mercancia = models.TextField(verbose_name='Descripción Comercial')
    partida_arancelaria = models.CharField(max_length=10)
    pais_origen = models.CharField(max_length=2)  # Código ISO
    pais_procedencia = models.CharField(max_length=2)
    cantidad = models.DecimalField(max_digits=12, decimal_places=3)
    unidad_medida = models.CharField(max_length=10)
    peso_bruto = models.DecimalField(max_digits=12, decimal_places=3)
    peso_neto = models.DecimalField(max_digits=12, decimal_places=3)
    
    # Valores
    valor_fob = models.DecimalField(max_digits=15, decimal_places=2)
    valor_cif = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        null=True,
        blank=True
    )
    tipo_cambio = models.DecimalField(max_digits=8, decimal_places=4)
    
    # Datos del despacho
    aduana_registro = models.CharField(max_length=50)
    numero_manifiesto = models.CharField(max_length=50, blank=True)
    fecha_llegada = models.DateField(null=True, blank=True)
    
    # Estados y seguimiento
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES,
        default='BORRADOR'
    )
    numero_dim = models.CharField(
        max_length=50, 
        blank=True,
        verbose_name='Número DIM/DUI'
    )
    canal_asignado = models.CharField(
        max_length=10,
        choices=CANAL_CHOICES,
        blank=True
    )
    
    # Auditoría
    usuario_creacion = models.ForeignKey(
        User, 
        on_delete=models.PROTECT,
        related_name='despachos_creados'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Despacho Aduanero'
        verbose_name_plural = 'Despachos Aduaneros'
        
    def __str__(self):
        return f"{self.numero_referencia} - {self.get_tipo_declaracion_display()}"
    

class LiquidacionAduanera(models.Model):
    despacho = models.OneToOneField(
        DespachoAduanero, 
        on_delete=models.CASCADE,
        related_name='liquidacion'
    )
    
    # Gravamen Aduanero (GA)
    gravamen_aduanero = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    # Impuesto al Valor Agregado (IVA)
    iva = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    # Impuesto al Consumo Específico (ICE)
    ice = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    # Impuesto Especial a los Hidrocarburos (IEHD)
    iehd = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
    # Totales
    total_tributos = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Pago
    pagado = models.BooleanField(default=False)
    fecha_pago = models.DateTimeField(null=True, blank=True)
    numero_comprobante_pago = models.CharField(max_length=50, blank=True)
    
    class Meta:
        verbose_name = 'Liquidación Aduanera'
        verbose_name_plural = 'Liquidaciones Aduaneras'
    
    def save(self, *args, **kwargs):
        self.total_tributos = (
            self.gravamen_aduanero + 
            self.iva + 
            self.ice + 
            self.iehd
        )
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Liquidación - {self.despacho.numero_referencia}"


class DocumentoDespacho(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('FACTURA', 'Factura Comercial'),
        ('BL', 'Bill of Lading'),
        ('GUIA_AEREA', 'Guía Aérea'),
        ('CRT', 'Carta de Porte'),
        ('PACKING', 'Lista de Empaque'),
        ('DAV', 'Declaración Andina de Valor'),
        ('POLIZA', 'Póliza de Seguro'),
        ('CERT_ORIGEN', 'Certificado de Origen'),
        ('SENASAG', 'Certificado SENASAG'),
        ('OTRO', 'Otro Documento'),
    ]
    
    despacho = models.ForeignKey(
        DespachoAduanero, 
        on_delete=models.CASCADE,
        related_name='documentos'
    )
    tipo_documento = models.CharField(
        max_length=20,
        choices=TIPO_DOCUMENTO_CHOICES
    )
    numero_documento = models.CharField(max_length=100)
    fecha_emision = models.DateField()
    archivo = models.FileField(
        upload_to='despachos/documentos/%Y/%m/',
        null=True,
        blank=True
    )
    observaciones = models.TextField(blank=True)
    fecha_carga = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['despacho', 'tipo_documento', 'numero_documento']
        verbose_name = 'Documento del Despacho'
        verbose_name_plural = 'Documentos del Despacho'
        ordering = ['tipo_documento', 'fecha_emision']
    
    def __str__(self):
        return f"{self.get_tipo_documento_display()} - {self.numero_documento}"