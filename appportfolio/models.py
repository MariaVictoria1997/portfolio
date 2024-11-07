# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
################################################
# Tabla 1- Habilidades 
################################################

class Habilidad(models.Model):  #la clase con su herencia 
    id = models.AutoField(primary_key=True) #AutoField es poner primary_key
    habilidad = models.CharField("nombre habilidad",max_length=25, null=True, blank=True) #CharField es un varchar
    nivel= models.IntegerField(null=True, blank=True) #null=true blank=true es para que no pete la base de datos ya que permite nulos y espacios en blanco
    comentario = models.TextField("Comentario", null=True, blank=True, max_length=255)

    class Meta: #clase anidada que configura a la otra clase
        verbose_name = "Habilidad"  #puede ser otro nombre
        verbose_name_plural = "Habilidades"
        ordering = ['habilidad']
		
    def __str__(self): #este es un metodo que pertenece a la clase y es el toString de java, el self es el this
        return "%s,%s,%s" % (self.habilidad, self.nivel, self.comentario)

################################################
# Tabla 2 Categorias
################################################

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField es poner primary_key
    nombre_categoria = models.CharField("Puesto de trabajo",max_length=30, null=True, blank=True)

    class Meta: #clase anidada que configura a la otra clase
        verbose_name = "Categoria"  #puede ser otro nombre
        verbose_name_plural = "Categorias"
        ordering = ['nombre_categoria']
    def __str__(self): #este es un metodo que pertenece a la clase y es el toString de java, el self es el this
        return "%s,%s" % (self.id,self.nombre_categoria)

################################################
# Tabla 3 Personal
################################################

class Personal(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField es poner primary_key
    nombre = models.CharField("Nombre", max_length=30, null=True, blank=True)
    apellido1 = models.CharField("Apellido1", max_length=30, null=True, blank=True)
    apellido2 = models.CharField("Apellido2", max_length=30, null=True, blank=True)
    edad = models.IntegerField("Edad", null=True, blank=True)
    #relacción de base de datos: ForeignKey
    usuario = models.ForeignKey(User, related_name='datos_usuario', null=True, blank=True, on_delete=models.PROTECT)

                                                                                            #protege de un borrado en cascada
    class Meta:  # clase anidada que configura a la otra clase
        verbose_name = "Personal"  # puede ser otro nombre
        verbose_name_plural = "Personales"
        ordering = ['nombre']

    def __str__(self):  # este es un metodo que pertenece a la clase y es el toString de java, el self es el this
        return "%s,%s,%s,%s,%s" % (self.id, self.nombre, self.apellido1, self.apellido2, self.edad)

################################################
# Tabla 4 Estudio
################################################

class Estudio(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField crea automáticamente un campo de clave primaria
    titulacion = models.CharField("Titulación", max_length=200, null=True, blank=True)
    fechaInicio = models.DateField("Fecha de Inicio", null=True, blank=True)
    fechaFin = models.DateField("Fecha de Fin", null=True, blank=True)
    notaMedia = models.DecimalField("Nota Media", max_digits=4, decimal_places=2, null=True, blank=True)
    lugarEstudio = models.CharField("Lugar estudio", max_length=200, null=True, blank=True)
    nombreLugar = models.CharField("Nombre del Lugar", max_length=200, null=True, blank=True)
    ciudad = models.CharField("Ciudad", max_length=100, null=True, blank=True)
    presencial = models.BooleanField("Es Presencial", default=True)
    observaciones = models.TextField("Observaciones", null=True, blank=True)

    class Meta:
        verbose_name = "Estudio"  # Nombre singular para el modelo
        verbose_name_plural = "Estudios"  # Nombre plural para el modelo
        ordering = ['-id']  # Ordena de manera descendente por 'id' (los registros más recientes primero)

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %  (self.id, self.titulacion, self.fechaInicio, self.fechaFin, self.notaMedia, self.lugarEstudio,self.nombreLugar, self.ciudad, self.presencial, self.observaciones)

################################################
# Tabla 5 Experiencia
################################################

class Experiencia(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.CharField('Empresa', max_length=50, null=True, blank=True)
    fecha_inicio = models.DateField('Fecha de Inicio', null=True, blank=True)
    fecha_fin = models.DateField('Fecha de Finalización', null=True, blank=True)
    observaciones = models.CharField('Funciones', max_length=50, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, related_name='expe_categoria', null=True, blank=True,
                                      on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Experiencia'  # puede ser otro nombre
        verbose_name_plural = 'Experiencias'
        ordering = ['empresa']

    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.id,self.empresa,self.fecha_inicio,self.fecha_fin,self.observaciones,self.categoria)

#class Persona(models.Model):
    #nombre = models.CharField(max_length=100)
    #ap1 = models.CharField(max_length=100)
    #ap2 = models.CharField(max_length=100)
    #edad = models.IntegerField()

    #def __str__(self):
        #return f'{self.nombre}{self.ap1}{self.ap2}'
################################################
# Tabla 5 Imagen
################################################
class Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField("Imagen", blank=True, null=True, upload_to="imagenes/")  # Campo para la imagen del diploma
    #estudio = models.ForeignKey(Estudio, related_name="estudio_imagenes", on_delete=models.CASCADE)  # Relación con el modelo 'Estudio'
    comentario = models.CharField('Comentario', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"
        ordering = ['id']

    def __str__(self):
        return "%s,%s,%s" % (self.id, self.imagen, self.comentario) #self.estudio
    ################################################
    # Tabla 6 Video
    ################################################
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.FileField("Video", blank=True, null=True, upload_to="videos/")
    comentario = models.CharField('Comentario', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        ordering = ['id']
    def __str__(self):
        return "%s,%s,%s" % (self.id, self.video, self.comentario)
################################################
# Tabla 7 Entrevistador
################################################
class Entrevistador(models.Model):
    id = models.AutoField(primary_key=True)
    avatar = models.ImageField('Avatar',blank=True, null=True, upload_to="media/")
    empresa = models.CharField('Empresa',max_length=30, null=True, blank=True)
    fecha_entrevista = models.DateField('Fecha Entrevista',null=True, blank=True)
    conectado = models.BooleanField('Conectado',null=True, blank=True)
    seleccionado = models.BooleanField('Seleccionado', null=True, blank=True)
    # Forteigns keys requerido desde djando 2.0
    user = models.ForeignKey(User, related_name="entrevistados_usuario",
    null=True, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Entrevistador"
        verbose_name_plural = "Entrevistadores"
        ordering = ['empresa']
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.id, self.empresa, self.fecha_entrevista, self.conectado, self.seleccionado, self.user)


