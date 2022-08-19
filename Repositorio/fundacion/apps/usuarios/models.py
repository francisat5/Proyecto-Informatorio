from django.db import models

from django.contrib.auth.models import AbstractUser 

class Usuario(AbstractUser):
	pass

"""CARGOS_CHOICES = (
    ("A", "ADMIN"),
    ("V", "VISITANTE")
)

class usuarios (models.Model):
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=13)
    contraseña = models.CharField(max_length=60)
    usuarios = models.CharField(max_length=50)
    tipoUsuario = models.CharField(max_length=1, choices=CARGOS_CHOICES, default="V")"""
