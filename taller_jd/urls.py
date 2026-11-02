from django.contrib import admin
from django.urls import path, include # <-- Importante agregar include
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from seguridad import views


urlpatterns = [
    # Redirigir la raíz (/) al login
    path('', RedirectView.as_view(pattern_name='login', permanent=False)), 
    
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='seguridad/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clientes/', include('clientes.urls')), # <-- Nueva ruta
]