# Generated by Django 3.2.8 on 2023-07-29 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idSolicitud', models.IntegerField(verbose_name='Id Solicitud')),
                ('fechaSolicitud', models.DateTimeField()),
                ('idUsuario', models.CharField(max_length=100, verbose_name='Descipción')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descipción')),
                ('fotoUbicacion', models.ImageField(null=True, upload_to='imagenes/')),
                ('direccionIncidente', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('idSeguimiento', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUsuario', models.CharField(max_length=100, verbose_name='Descipción')),
                ('fechaSeguimiento', models.DateTimeField()),
                ('descripcionSeguimiento', models.CharField(max_length=200, verbose_name='Descipción')),
                ('idSolicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FK_Solicitud_Seguimiento', to='reportes311.solicitud')),
            ],
        ),
    ]
