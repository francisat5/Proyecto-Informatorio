
from django.shortcuts import render


from .models import Somos

def Quienes(request):
	ctx = {}	
	
	todas = Somos.objects.all()
	
	ctx['notis'] = todas

	return render(request,'quienes_somos.html',ctx)
