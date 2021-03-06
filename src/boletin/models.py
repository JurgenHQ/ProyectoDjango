from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registrado(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True) #Crea los atributos en la base de datos
    email = models.EmailField()
    timeestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

    def __unicode__(self): #Python 2 
        return self.email 

    def __str__(self): #Python 3
        return self.email