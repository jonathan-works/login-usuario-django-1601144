from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioPersonalizado(AbstractUser):
    idade = models.PositiveIntegerField(null=True, blank=True)
