# backend/apps/clients/models.py
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model

User = get_user_model()

class Cliente(models.Model):
    TIPO_OPERADOR_CHOICES = [
        ('IMP', 'Importador'),
        ('EXP', 'Exportador'),
        ('BOTH', 'Importador/Exportador'),
    ]
    
    TIPO_CLIENTE_CHOICES = [
        ('REGULAR', 'Regular'),
        ('VIP', 'VIP'),
        ('NUEVO', 'Nuevo'),
    ]
    
    ESTADO_CHOICES = [
        ('ACTIVO', 'Activo'),
        ('INACTIVO', 'Inactivo'),
        ('SUSPENDIDO', 'Suspendido'),
    ]
    
    VOLUMEN_CHOICES = [
        ('BAJO', 'Bajo'),
        ('MEDIO', 'Medio'),
        ('ALTO', 'Alto'),
    ]
    
    # Campos existentes
    nit = models.CharField(
        max_length=15,
        unique=True,
        validators=[MinLengthValidator(7)],
        verbose_name='NIT'
    )
    razon_social = models.CharField(max_length=200)
    nombre_comercial = models.CharField(max_length=200, blank=True)  # NUEVO
    direccion_legal = models.TextField()
    ciudad = models.CharField(max_length=100, default='Santa Cruz')  # NUEVO
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    representante_legal = models.CharField(max_length=100)
    ci_representante = models.CharField(max_length=20)
    
    # Campos de categorización
    tipo_operador = models.CharField(
        max_length=4,
        choices=TIPO_OPERADOR_CHOICES,
        default='IMP'
    )
    tipo_cliente = models.CharField(  # NUEVO
        max_length=20,
        choices=TIPO_CLIENTE_CHOICES,
        default='REGULAR'
    )
    estado = models.CharField(  # NUEVO
        max_length=20,
        choices=ESTADO_CHOICES,
        default='ACTIVO'
    )
    volumen_operaciones = models.CharField(  # NUEVO
        max_length=10,
        choices=VOLUMEN_CHOICES,
        default='MEDIO'
    )
    
    # Timestamps
    fecha_registro = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)  # NUEVO
    updated_at = models.DateTimeField(auto_now=True)  # NUEVO
    
    # Campo anterior para compatibilidad
    activo = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['razon_social']
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return f"{self.nit} - {self.razon_social}"


class ContactoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contactos')
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    celular = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    es_principal = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Contacto del Cliente'
        verbose_name_plural = 'Contactos del Cliente'
    
    def __str__(self):
        return f"{self.nombre} - {self.cliente.razon_social}"


class EvaluacionCliente(models.Model):
    CALIFICACION_CHOICES = [
        ('EXCELENTE', 'Excelente'),
        ('BUENO', 'Bueno'),
        ('REGULAR', 'Regular'),
        ('MALO', 'Malo'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='evaluaciones')
    fecha_evaluacion = models.DateField()
    calificacion = models.CharField(max_length=20, choices=CALIFICACION_CHOICES)
    puntaje = models.IntegerField(default=0)
    observaciones = models.TextField(blank=True)
    evaluado_por = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Evaluación del Cliente'
        verbose_name_plural = 'Evaluaciones del Cliente'
        ordering = ['-fecha_evaluacion']
    
    def __str__(self):
        return f"Evaluación {self.cliente.razon_social} - {self.calificacion}"