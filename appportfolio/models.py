# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

################################################
# Habilidades
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
# Categorias
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
# Personal
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
# Estudio
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
# Experiencia
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
# Imagen
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
    # Video
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
# Entrevistador
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
################################################
# CURRICULUM
################################################

class Curriculum(models.Model):
    id = models.AutoField(primary_key=True)  # Aquí se corrigió "true" por "True"
    nombre = models.CharField("Nombre",max_length=100, null=True,blank=True)
    ap1 = models.CharField("Apellido1",max_length=100, null=True,blank=True)
    ap2 = models.CharField("Apellido2",max_length=100, null=True,blank=True)
    email = models.EmailField("Email",max_length=100, null=True,blank=True)
    telefono = models.CharField("Telefono",max_length=100, null=True,blank=True)

    class Meta:
        verbose_name = "Curriculum"
        verbose_name_plural = "Curriculums"
        ordering = ['id']

    def __str__(self):
        return f"{self.id}{self.nombre} {self.ap1} {self.ap2}{self.email}{self.telefono}"


class DetalleCurriculumEstudio(models.Model):
    id = models.AutoField(primary_key=True)
    estudio = models.ForeignKey(Estudio, related_name='estudio_detalle', null=True,blank=True, on_delete=models.PROTECT)
    curriculum = models.ForeignKey(Curriculum, related_name='curriculum_detalle', null=True,blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "DetalleCurriculumEstudio"
        verbose_name_plural = "DetalleCurriculumEstudios"
        ordering = ['id']

    def __str__(self):
        # Ajusta esto según el atributo que exista en el modelo Estudio
        return f"{self.id}{self.estudio.titulacion} para {self.curriculum.nombre}"


class DetalleCurriculumExperiencia(models.Model):
    id = models.AutoField(primary_key=True)  # Aquí también se corrigió
    experiencia = models.ForeignKey(Experiencia, related_name='experiencia_detalle', null=True,blank=True, on_delete=models.PROTECT)  # Corregido
    curriculum = models.ForeignKey(Curriculum, related_name='curriculum_detalles', null=True,blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "DetalleCurriculumExperiencia"
        verbose_name_plural = "DetalleCurriculumExperiencias"
        ordering = ['id']

    def __str__(self):
        return f"{self.experiencia.empresa} para {self.curriculum.nombre}"
################################################
# NOTICIAS
################################################
class Noticia(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField('Imagen', blank=True, null =True, upload_to="media/")
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['id']
    def __str__(self):
        return self.titulo
################################################
# VALORACIONES
################################################
class Valoracion(models.Model):
    id = models.AutoField(primary_key=True)
    votos_entrevista = models.DecimalField(
        "Votos Entrevista", max_digits=5, decimal_places=2, null=True, blank=True
    )
    votos_empresa = models.DecimalField(
        "Votos Empresa", max_digits=5, decimal_places=1, null=True, blank=True
    )
    media_aspectos = models.DecimalField(
        "Media Aspectos", max_digits=5, decimal_places=2, null=True, blank=True
    )
    entrevista = models.CharField(
        "Descripción Entrevista", max_length=300, null=True, blank=True
    )
    empresa = models.CharField(
        "Descripción Empresa", max_length=200, null=True, blank=True
    )
    valoraciones = models.IntegerField(
        "Nº Valoraciones", null=True, blank=True
    )
    timestamp = models.DateTimeField("Fecha", default=timezone.now)

    class Meta:
        verbose_name = "Valoracion"
        verbose_name_plural = "Valoraciones"
        ordering = ['id']

    def __str__(self):
        return (
            f"ID: {self.id}, "
            f"Votos Entrevista: {self.votos_entrevista}, "
            f"Votos Empresa: {self.votos_empresa}, "
            f"Media Aspectos: {self.media_aspectos}, "
            f"Entrevista: {self.entrevista}, "
            f"Fecha: {self.timestamp}"
        )
################################################
#  CHAT
################################################

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, related_name='mensajes_enviados', on_delete=models.CASCADE)
    destinatario = models.ForeignKey(User, related_name='mensajes_recibidos',on_delete=models.CASCADE)
    contenido = models.TextField('Contenido del mensaje')
    fecha_envio = models.DateTimeField('Fecha de envío', auto_now_add=True)
    leido = models.BooleanField('Leido', default=False)

    class Meta:
        ordering = ['fecha_envio']
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        ordering = ['id']
    def __str__(self):
        return f"De: {self.remitente.username} Para: {self.destinatario.username} - {self.contenido[:30]}"


class Estado(models.Model):
    ESTADO_CHOICES = [
        ('P', 'Pendiente'),
        ('R', 'Realizado'),
        ('E', 'Empezando'),
    ]
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default='P')
    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ['id']
    def __str__(self):
        return self.get_estado_display()
################################################
# TAREAS
################################################

class Tarea(models.Model):
    tarea = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True, blank=True)
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"
        ordering = ['id']
    def __str__(self):
        return self.tarea

################################################
# CALIFICACIONES
################################################
class Calificacion(models.Model):
    id = models.AutoField(primary_key=True)
    asignatura = models.CharField(max_length=200)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        verbose_name = "Calificacion"
        verbose_name_plural = "Calificaciones"
        ordering = ['id']

    def __str__(self):
        return f"{self.asignatura} - {self.nota}"
################################################
# PROYECTOS
################################################
class Proyecto(models.Model):
    titulo = models.CharField(max_length=255)
    lenguaje = models.CharField(max_length=100)
    tecnologias = models.TextField()
    observaciones = models.TextField(blank=True, null=True)
    fecha_publicacion = models.DateField()

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ['id']

    def __str__(self):
        return self.titulo