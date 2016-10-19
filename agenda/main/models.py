from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
	nombre=models.CharField(max_length=140)
	desc=models.TextField()
	precio=models.CharField(max_length=140)	

	def __str__(self):
		return self.nombre