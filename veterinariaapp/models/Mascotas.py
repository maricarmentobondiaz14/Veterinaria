from django.db import models
from veterinariaapp.models.Usuarios import Usuarios

class Mascotas(models.Model):
    id_mascota = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=12)
    usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='usuario')
    tipo_animal = models.CharField(max_length=12)
    raza = models.CharField(max_length=20, blank=True, null=True)
    genero = models.CharField(max_length=30)
    esterilizado = models.IntegerField(blank=True, null=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=5)
    peso = models.DecimalField(max_digits=10, decimal_places=5)
    vacunas = models.CharField(max_length=30)
    imagen = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mascotas'