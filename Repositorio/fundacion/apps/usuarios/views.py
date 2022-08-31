from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView

from .models import Usuario
from .forms import registrarForm

class registrar(CreateView):
    model = Usuario
    template_name = "usuarios/registrar.html"
    form_class = registrarForm 

    def get_success_url(self, **kwargs):
        return reverse('home')
