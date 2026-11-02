from django.contrib import admin
from .models import Cliente, Vehiculo

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('numero_documento', 'nombre_completo', 'telefono')
    search_fields = ('numero_documento', 'nombre_completo')

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'cliente')
    search_fields = ('placa', 'marca')