# Generated by Django 5.1.1 on 2024-10-10 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(blank=True, max_length=30, null=True, verbose_name='Puesto de trabajo')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nombre_categoria'],
            },
        ),
        migrations.CreateModel(
            name='Estudio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulacion', models.CharField(blank=True, max_length=200, null=True, verbose_name='Titulación')),
                ('fechaInicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('fechaFin', models.DateField(blank=True, null=True, verbose_name='Fecha de Fin')),
                ('notaMedia', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Nota Media')),
                ('lugarEstudio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Lugar estudio')),
                ('nombreLugar', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre del Lugar')),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True, verbose_name='Ciudad')),
                ('presencial', models.BooleanField(default=True, verbose_name='Es Presencial')),
                ('observaciones', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': 'Estudio',
                'verbose_name_plural': 'Estudios',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('habilidad', models.CharField(blank=True, max_length=25, null=True, verbose_name='nombre habilidad')),
                ('nivel', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
                'ordering': ['habilidad'],
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nombre')),
                ('apellido1', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nombre')),
                ('apellido2', models.CharField(blank=True, max_length=30, null=True, verbose_name='Nombre')),
                ('edad', models.IntegerField(blank=True, null=True, verbose_name='Edad')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('empresa', models.CharField(blank=True, max_length=50, null=True, verbose_name='Empresa')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('fecha_fin', models.DateField(blank=True, null=True, verbose_name='Fecha de Finalización')),
                ('observaciones', models.CharField(blank=True, max_length=50, null=True, verbose_name='Funciones')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expe_categoria', to='appportfolio.categoria')),
            ],
            options={
                'verbose_name': 'Experiencia',
                'verbose_name_plural': 'Experiencias',
                'ordering': ['empresa'],
            },
        ),
    ]