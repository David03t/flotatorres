from django.db import models


class Usuarios(models.Model):
    id = models.AutoField(primary_key= True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=30)
    edad = models.IntegerField()
    tipo_de_documento = models.IntegerField()
    numero_de_documento = models.BigIntegerField()
    tipo_de_persona = models.IntegerField(default=1)
    rh = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuarios'

class TipoDocumentos(models.Model):
    tipo_documento = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'tipo_documentos'

class TipoSangre(models.Model):
    tipo_rh = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'tipo_sangre'