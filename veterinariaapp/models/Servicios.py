from django.db import models

class Servicios(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    precioxservicio = models.DecimalField(max_digits=30, decimal_places=2)
    descripcion = models.CharField(max_length=4000)
    imagen = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicios'