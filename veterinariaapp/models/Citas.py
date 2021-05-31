from django.db import models
from veterinariaapp.models.Usuarios import Usuarios
from veterinariaapp.models.Servicios import Servicios
from veterinariaapp.models.Mascotas import Mascotas

class Citas(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_servicio = models.ForeignKey(Servicios, models.DO_NOTHING, db_column='id_servicio')
    usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='usuario')
    id_mascota = models.ForeignKey(Mascotas, models.DO_NOTHING, db_column='id_mascota')
    fecha = models.DateField()

    class Meta:
        managed = False
        db_table = 'citas'