from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),
    path('nuevo/', views.crear_cliente, name='crear_cliente'),
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'), # <-- Nueva
    path('vehiculos/nuevo/', views.crear_vehiculo, name='crear_vehiculo'), # <-- Nueva
]