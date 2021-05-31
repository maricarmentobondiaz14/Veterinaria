from django.db import models

class Usuarios(models.Model):
    usuario = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    tipousuario = models.IntegerField(db_column='tipoUsuario', blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=20)
    codigopostal = models.IntegerField(db_column='codigoPostal')  # Field name made lowercase.
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'