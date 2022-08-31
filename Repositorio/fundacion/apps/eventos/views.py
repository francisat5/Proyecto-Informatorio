from django.shortcuts import render
from .models import Eventos

def eventos(request):
	ctx = {}
	todos = Eventos.objects.all() 
	print(todos)

	ctx['evento'] = todos

	return render(request,'eventos/eventos_listar.html',ctx)
