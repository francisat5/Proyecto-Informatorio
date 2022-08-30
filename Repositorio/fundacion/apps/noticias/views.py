from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Noticia, Comentario


def Listar(request):
 	#Creo el diccionario para pasar datos al temaplte
	ctx = {}	
	#BUSCAR LO QUE QUIERO EN LA BD
	todas = Noticia.objects.all()
	print(todas)
	#PASARLO AL TEMPLATE
	ctx['notis'] = todas

	return render(request,'noticias/listar_noticias.html',ctx)

class Detalle_Noticia(LoginRequiredMixin, DetailView):
	model = Noticia
	template_name = 'noticias/detalle_noticia.html'

def Agregar_Comentario(request,pk):
	texto_comentario = request.POST.get('comment')
	
	noti = Noticia.objects.get(pk = pk)

	c = Comentario.objects.create(noticia = noti, texto = texto_comentario, usuario = request.user)

	return HttpResponseRedirect(reverse_lazy('noticias:detalle_noticias', kwargs={'pk':pk}))


