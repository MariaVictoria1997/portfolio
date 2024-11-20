# -*- coding: utf-8 -*-
from django.contrib import admin
from appportfolio.models import *
from django.contrib.auth.models import User
#from __future__ import unicode_literals


admin.site.site_header = "Sitio web Salmantino"  #este es el título
admin.site.site_title = "Portal de Portfolio"
admin.site.index_title = "Bienvenidos al portal de Administración"

class HabilidadAdmin(admin.ModelAdmin):
    list_display = ['id','habilidad']
    search_fields = ('id','habilidad') #siempre tienen que ser una tupla
    list_filter   = ('id','habilidad') #siempre tienen que ser una tupla
admin.site.register(Habilidad, HabilidadAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre_categoria']
    search_fields = ('id','nombre_categoria') #siempre tienen que ser una tupla
    list_filter   = ('id','nombre_categoria') #siempre tienen que ser una tupla
admin.site.register(Categoria, CategoriaAdmin)

class PersonalAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','apellido1','apellido2','edad']
    search_fields = ('id','nombre','apellido1','apellido2','edad') #siempre tienen que ser una tupla
    list_filter   = ('id','nombre','apellido1','apellido2','edad') #siempre tienen que ser una tupla
admin.site.register(Personal, PersonalAdmin)

class EstudiosAdmin(admin.ModelAdmin):
    list_display = ['id','titulacion','fechaInicio','fechaFin','notaMedia','lugarEstudio','nombreLugar','ciudad','presencial','observaciones']
    search_fields = ('id','titulacion','fechaInicio','fechaFin','notaMedia','lugarEstudio','nombreLugar','ciudad','presencial','observaciones') #siempre tienen que ser una tupla
    list_filter   = ('id','titulacion','fechaInicio','fechaFin','notaMedia','lugarEstudio','nombreLugar','ciudad','presencial','observaciones') #siempre tienen que ser una tupla
admin.site.register(Estudio, EstudiosAdmin)

class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ['id','empresa','fecha_inicio','fecha_fin','observaciones','categoria']
    search_fields = ('id','empresa','fecha_inicio','fecha_fin','observaciones','categoria') #siempre tienen que ser una tupla
    list_filter   = ('id','empresa','fecha_inicio','fecha_fin','observaciones','categoria') #siempre tienen que ser una tupla
admin.site.register(Experiencia, ExperienciaAdmin)

class ImagenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Imagen._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id', 'imagen') #siempre tienen que ser una tupla
    #list_filter   = ('id', 'imagen', 'estudio') #siempre tienen que ser una tupla
admin.site.register(Imagen, ImagenAdmin)

class VideoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Video._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id', 'video') #siempre tienen que ser una tupla
admin.site.register(Video, VideoAdmin)

class EntrevistadorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Entrevistador._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id','empresa')
admin.site.register(Entrevistador, EntrevistadorAdmin)

class CurriculumAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'ap1', 'ap2', 'email', 'telefono']
    search_fields = ('id', 'nombre', 'ap1', 'ap2', 'email', 'telefono')  # Siempre deben ser tuplas
    list_filter = ('id', 'nombre', 'ap1', 'ap2')  # Siempre deben ser tuplas

admin.site.register(Curriculum, CurriculumAdmin)

class DetalleCurriculumEstudioAdmin(admin.ModelAdmin):
    list_display = ['id', 'estudio', 'curriculum']
    search_fields = ('id', 'estudio__nombre', 'curriculum__nombre')  # Acceso a campos relacionados
    list_filter = ('estudio', 'curriculum')

admin.site.register(DetalleCurriculumEstudio, DetalleCurriculumEstudioAdmin)

class DetalleCurriculumExperienciaAdmin(admin.ModelAdmin):
    list_display = ['id', 'experiencia', 'curriculum']
    search_fields = ('id', 'experiencia__empresa', 'curriculum__nombre')  # Acceso a campos relacionados
    list_filter = ('experiencia', 'curriculum')

admin.site.register(DetalleCurriculumExperiencia, DetalleCurriculumExperienciaAdmin)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Noticia._meta.get_fields() if hasattr(field, 'verbose_name')]
    search_fields = ('id','titulo')
admin.site.register(Noticia, NoticiaAdmin)

@admin.register(Valoracion)
class ValoracionAdmin(admin.ModelAdmin):
    list_display = ("id", "votos_entrevista", "votos_empresa", "media_aspectos", "timestamp")
    readonly_fields = ('media_aspectos',)

    def save_model(self, request, obj, form, change):
        # Calcula automáticamente la media antes de guardar
        if obj.votos_entrevista and obj.votos_empresa:
            obj.media_aspectos = (obj.votos_entrevista + obj.votos_empresa) / 2
        super().save_model(request, obj, form, change)
