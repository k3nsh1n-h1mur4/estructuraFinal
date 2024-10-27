from django.db import models

from django.contrib.auth.models import User


class User(models.Model):
    pass

class EstructuraModel(models.Model):
    class Meta:
        db_table = 'estructuratbl'
        
    matricula = models.CharField(max_length=250, null=True, blank=True)
    nombre = models.CharField(max_length=250, null=True, blank=True)
    fotot = models.CharField(max_length=250, null=True, blank=True)
    fotof = models.CharField(max_length=250, null=True, blank=True)
    fechan = models.CharField(max_length=250, null=True, blank=True)
    categoria = models.CharField(max_length=250, null=True, blank=True)
    centtrabact = models.CharField(max_length=250, null=True, blank=True)
    adscant = models.CharField(max_length=250, null=True, blank=True)
    turno = models.CharField(max_length=250, null=True, blank=True)
    domicilio = models.CharField(max_length=250, null=True, blank=True)
    colonia = models.CharField(max_length=250, null=True, blank=True)
    municipio = models.CharField(max_length=250, null=True, blank=True)
    seccional = models.CharField(max_length=250, null=True, blank=True)
    numcel = models.CharField(max_length=250, null=True, blank=True)
    correo = models.CharField(max_length=250, null=True, blank=True)
    resp100 = models.CharField(max_length=250, null=True, blank=True)
    resp10 = models.CharField(max_length=250, null=True, blank=True)
    parttrab = models.CharField(max_length=250, null=True, blank=True)
    infadic = models.CharField(max_length=250, null=True, blank=True)
    descansos = models.CharField(max_length=250, null=True, blank=True)
    vacprog = models.CharField(max_length=250, null=True, blank=True)
    servicio = models.CharField(max_length=250, null=True, blank=True)
    promocion = models.CharField(max_length=250, null=True, blank=True)
    movilizacion = models.CharField(max_length=250, null=True, blank=True)
    respasig = models.CharField(max_length=250, null=True, blank=True)
    engrupo = models.CharField(max_length=250, null=True, blank=True)
    asisreunion = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

