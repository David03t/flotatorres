# Generated by Django 4.0.4 on 2022-06-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('telefono', models.BigIntegerField(max_length=20)),
                ('correo', models.EmailField(max_length=30)),
                ('edad', models.IntegerField(max_length=11)),
                ('tipo_de_documento', models.IntegerField(max_length=11)),
                ('numero_de_documento', models.BigIntegerField(max_length=20)),
                ('tipo_de_persona', models.IntegerField(max_length=11)),
                ('rh', models.IntegerField(max_length=11)),
            ],
        ),
    ]
