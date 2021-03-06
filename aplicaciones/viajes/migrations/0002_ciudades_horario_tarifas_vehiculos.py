# Generated by Django 4.0.4 on 2022-06-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=20)),
                ('despachador', models.IntegerField()),
            ],
            options={
                'db_table': 'ciudades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_salida', models.CharField(max_length=7)),
                ('limite', models.IntegerField()),
            ],
            options={
                'db_table': 'horario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tarifas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precios', models.IntegerField()),
            ],
            options={
                'db_table': 'tarifas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('generacion', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('placa', models.CharField(max_length=6)),
                ('kilometraje', models.IntegerField()),
            ],
            options={
                'db_table': 'vehiculos',
                'managed': False,
            },
        ),
    ]
