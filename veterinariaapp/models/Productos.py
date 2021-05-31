from django.db import models

class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    referencia = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=30)
    marca = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'