# -*-coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin # sirve para trabajar con el modulo de administración
from django.urls import path, include, re_path #el bueno es el re_path
from appportfolio import views #sirve para importar las vistas
from appportfolio.views import * #siempre se importa todo con el *
# servicio de ficheros estáticos durante el desarrollo
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
# servicio de ficheros estáticos durante el servidor
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),  # este redirige al admin
    re_path(r'^$', views.home, name='home'),  # este redirige al home
    re_path('sobremi/', views.sobremi, name='sobremi'),
    re_path('estudios/', views.estudios, name='estudios'),  # Asegúrate de que sea estudios y no estudios_view
    re_path(r'^(?P<id>\d+)/ver_experiencia$', views.ver_experiencia,name='ver_experiencia'),
    path('experiencia/', views.experiencia, name='experiencia'),
    path('eliminarExperiencia/<int:pk>/', views.eliminarExperiencia,name='eliminarExperiencia'),
    #path('ver_habilidad', views.ver_experiencia, name='ver_habilidad'),
    path('habilidad/<int:id>/', views.ver_habilidad, name='ver_habilidad'),
    path('habilidades/', views.habilidades, name='habilidades'),
    #path('eliminar_habilidad/<int:pk>/', views.eliminar_habilidad, name='eliminar_habilidad'),
    path('eliminar_habilidad/<int:pk>/', views.eliminar_habilidad, name='eliminar_habilidad'),
    path('persona/nueva/', views.crear_persona, name='crear_persona'),
    path('persona/editar/<int_persona_id>/', views.editar_persona, name='editar_persona'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('cerrar/', cerrar, name='cerrar'),
    path('subir_imagenes/', subir_imagenes, name='subir_imagenes'),
    path('imagen/editar/<int:imagen_id>/', views.editar_imagen, name='editar_imagen'),
    path('imagen/eliminar/<int:imagen_id>/', views.eliminar_imagen, name='eliminar_imagen'),
    path('subir_videos/', subir_videos, name='subir_videos'),
    path('video/editar/<int:video_id>/', views.editar_video, name='editar_video'),
    path('video/eliminar/<int:video_id>/', views.eliminar_video, name='eliminar_video'),
    path('contacto/', views.contacto, name='contacto'),
    # pk <int:pk> es tipo de dato y r'^(?P<id>\d+) es expresion regular
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root': settings.MEDIA_ROOT,
    })
]


