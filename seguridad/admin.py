from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Añadimos nuestros campos al formulario del admin
    fieldsets = UserAdmin.fieldsets + (
        ('Información del Taller', {'fields': ('rol', 'telefono')}),
    )
    list_display = ('username', 'email', 'rol', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)