import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class registrarForm(UserCreationForm):

    class Meta:

        model = Usuario
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]