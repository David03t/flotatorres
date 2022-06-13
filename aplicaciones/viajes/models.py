from django.db import models

# Create your models here.

class Viajes(models.Model):
    tarifa = models.IntegerField()
    id_ciudad_1 = models.CharField(max_length=255)
    id_ciudad_2 = models.CharField(max_length=255)
    id_hora = models.CharField(max_length=25)
    id_vehiculo = models.IntegerField()
    usuario_conductor = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'viajes'

class Vehiculos(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    generacion = models.IntegerField()
    capacidad = models.IntegerField()
    placa = models.CharField(max_length=6)
    kilometraje = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vehiculos'

class Tarifas(models.Model):
    precios = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarifas'

class Horario(models.Model):
    hora_salida = models.CharField(max_length=7)
    limite = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'horario'

class Ciudades(models.Model):
    ciudad = models.CharField(max_length=20)
    despachador = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ciudades'
        
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