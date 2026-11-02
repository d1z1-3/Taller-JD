from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Definimos los roles exactos del taller
    ROLES = (
        ('ADMIN', 'Administrador'),
        ('RECEP', 'Recepcionista'),
        ('MECAN', 'Mecánico'),
    )
    
    # Agregamos los campos extra
    rol = models.CharField(max_length=10, choices=ROLES, default='RECEP')
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"