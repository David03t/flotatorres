# Generated by Django 4.0.4 on 2022-06-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_usuarios_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documento', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'tipo_documentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoSangre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_rh', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'tipo_sangre',
                'managed': False,
            },
        ),
    ]
