from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from seguridad import views  # <-- Importamos nuestras vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='seguridad/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'), # <-- Nueva ruta
]