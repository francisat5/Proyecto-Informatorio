from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Noticia


def Listar(request):
 	#Creo el diccionario para pasar datos al temaplte
	ctx = {}	
	#BUSCAR LO QUE QUIERO EN LA BD
	todas = Noticia.objects.all()
	#PASARLO AL TEMPLATE
	ctx['notis'] = todas

	return render(request,'noticias/listar_noticias.html',ctx)



