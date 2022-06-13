# Generated by Django 4.0.4 on 2022-06-13 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketes', '0001_initial'),
    ]

    operations = [
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