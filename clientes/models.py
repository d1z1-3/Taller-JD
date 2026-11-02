from django.db import models

class Cliente(models.Model):
    TIPO_DOCUMENTO = (
        ('CC', 'Cédula de Ciudadanía'),
        ('NIT', 'NIT'),
        ('CE', 'Cédula de Extranjería'),
        ('PAS', 'Pasaporte'),
    )
    
    tipo_documento = models.CharField(max_length=5, choices=TIPO_DOCUMENTO, default='CC')
    numero_documento = models.CharField(max_length=20, unique=True)
    nombre_completo = models.CharField(max_length=150)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_completo} - {self.numero_documento}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class Vehiculo(models.Model):
    COMBUSTIBLE = (
        ('GAS', 'Gasolina'),
        ('DIS', 'Diésel'),
        ('ELE', 'Eléctrico'),
        ('HIB', 'Híbrido'),
    )
    
    placa = models.CharField(max_length=10, unique=True, primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    kilometraje = models.IntegerField(default=0)
    nivel_combustible = models.CharField(max_length=3, choices=COMBUSTIBLE, default='GAS')
    
    # Relación 1:N (Un cliente puede tener muchos vehículos)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='vehiculos')

    def __str__(self):
        return f"{self.placa} - {self.marca} {self.modelo}"

    class Meta:
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"