from django.db import models


class Eventos(models.Model):
	titulo = models.CharField(max_length = 120)
	fecha = models.DateField(auto_now_add = True)
	detalle = models.TextField()
	imagen = models.ImageField(upload_to = 'eventos', null=True, blank = True)

	def __str__(self):
		return self.titulo

