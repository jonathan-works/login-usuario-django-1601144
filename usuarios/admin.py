# Register your models here.
from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioPersonalizadoCreationForm
from .forms import UsuarioPersonalizadoChangeForm
from .models import UsuarioPersonalizado

class UsuarioPersonalizadoAdmin(UserAdmin):
    add_form = UsuarioPersonalizadoCreationForm
    add_form = UsuarioPersonalizadoChangeForm
    model = UsuarioPersonalizado

admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)