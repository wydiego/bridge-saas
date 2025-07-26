from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    role = models.CharField(
        max_length=50,
        choices=[
            ('admin', 'Administrador'),
            ('despachante_senior', 'Despachante Senior'),
            ('operador', 'Operador'),
            ('solo_lectura', 'Solo Lectura'),
        ],
        default='operador'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.get_full_name()} ({self.email})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
