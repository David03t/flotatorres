# Generated by Django 4.0.4 on 2022-06-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketes', '0002_vehiculos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viajes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarifa', models.IntegerField()),
                ('id_ciudad_1', models.CharField(max_length=255)),
                ('id_ciudad_2', models.CharField(max_length=255)),
                ('id_hora', models.CharField(max_length=25)),
                ('id_vehiculo', models.IntegerField()),
                ('usuario_conductor', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'viajes',
                'managed': False,
            },
        ),
    ]