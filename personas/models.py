from django.db import models

# Create your models here.
class TipoDocumento(models.Model):
	descripcion = models.CharField(max_length=200)
	# to string
	def __str__(self):
		return self.descripcion

class Provincia(models.Model):
	nombre = models.CharField(max_length=200)
	# to string
	def __str__(self):
		return self.nombre

class Localidad(models.Model):
	nombre = models.CharField(max_length=200)
	provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
	# to string
	def __str__(self):
		return self.nombre

class Persona(models.Model):
	tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
	numero_documento = models.IntegerField(blank=False, null=False)
	apellido = models.CharField(max_length=200)
	nombre = models.CharField(max_length=200)
	localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
	# to string
	def __str__(self):
		return self.apellido+", "+self.nombre
