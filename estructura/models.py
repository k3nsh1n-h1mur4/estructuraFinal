from django.db import models

from django.contrib.auth.models import User


class User(models.Model):
    pass

class EstructuraModel(models.Model):
    class Meta:
        db_table = 'estructurafinal'
        
    matricula = models.CharField(max_length=250, null=True, blank=True)
    nombre = models.CharField(max_length=250, null=True, blank=True)
    ftrab = models.CharField(max_length=250, null=True, blank=True)
    ffirma = models.CharField(max_length=250, null=True, blank=True)
    fnac = models.CharField(max_length=250, null=True, blank=True)
    categoria = models.CharField(max_length=250, null=True, blank=True)
    adsc_act = models.CharField(max_length=250, null=True, blank=True)
    adsc_ant = models.CharField(max_length=250, null=True, blank=True)
    turno = models.CharField(max_length=250, null=True, blank=True)
    domicilio = models.CharField(max_length=250, null=True, blank=True)
    colonia = models.CharField(max_length=250, null=True, blank=True)
    municipio = models.CharField(max_length=250, null=True, blank=True)
    seccional = models.CharField(max_length=250, null=True, blank=True)
    num_cel = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
    Resp_100 = models.CharField(max_length=250, null=True, blank=True)
    Resp_10 = models.CharField(max_length=250, null=True, blank=True)
    part_trab = models.CharField(max_length=250, null=True, blank=True)
    inf_adic = models.CharField(max_length=250, null=True, blank=True)
    descansos = models.CharField(max_length=250, null=True, blank=True)
    vac_prog = models.CharField(max_length=250, null=True, blank=True)
    servicio = models.CharField(max_length=250, null=True, blank=True)
    promocion = models.CharField(max_length=250, null=True, blank=True)
    movilizacion = models.CharField(max_length=250, null=True, blank=True)
    asis_reu = models.CharField(max_length=250, null=True, blank=True)
    voto_25Sept = models.CharField(max_length=250, null=True, blank=True)
    engrupo = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    inf_admin = models.CharField(max_length=250, null=True, blank=True)
    mi_resp = models.CharField(max_length=250, null=True, blank=True)
    user_id_id = models.ForeignKey("User", on_delete=models.CASCADE)

