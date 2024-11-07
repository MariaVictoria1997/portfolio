# -*-coding: utf-8 -*-
from __future__ import unicode_literals

import os
from lib2to3.fixes.fix_input import context
from django.conf import settings

from django.shortcuts import render
from django.http import HttpResponse
from appportfolio.models import *
from django.shortcuts import redirect
from django.core.paginator import Paginator
from .models import Estudio
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render
import urllib
# email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.

def home(request):
    print('Hola estoy en home')
    nombre ='vicky'
    actual =request.user
    idusuario = 0
    idusuario = actual.id
    request.session['idusuario']=idusuario
    numconectados = 0
    dato = ""
    #ip externa o publica
    lista = "0123456789."
    ip = ""
    try:
        dato = urllib.request.urlopen('https://www.wikipedia.org').headers['X-Client-IP']
        #dato = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        print("IP PUBLICA ="+str(dato))
    except:
        print("Error en la librería de la IP")
        dato = ""
    finally:
        print("USUARIO ACTUAL...["+str(actual)+"]")
    for x in str(dato):
        if x in lista:
            ip += x
    if str(actual)=="AnonymousUser":
        request.session['tipousuario'] = 'anonimo'
        print('IP ANONIMO...'+str(ip))
    usuario = 'prueba'
    context = {'nombre':nombre,'ip':ip}
    return render(request, 'home.html', context=context)

def habilidades(request):
    print('Hola estoy en habilidades')
    # select * from Habilidad order by habilidad desc| Habilidad: es la tabla, se coge el mismo nombre que en el modelo
    #habilidades: es un objeto de tipo queryset
    habilidades_list = Habilidad.objects.all().order_by('-habilidad') #este es el list
    #context = {'habilidades_list': habilidades}
    context = {'habilidades_list': habilidades_list}
    return render(request, 'habilidades.html', context=context)

def ver_habilidad(request, id):
    hab_id=id
    habilidad = Habilidad.objects.get(id=hab_id)
    context = {'habilidad': habilidad}
    return render(request, 'ver_habilidad.html',context=context)


def eliminar_habilidad(request, pk):
    print("ELIMINAR")
    hab_id = pk
    habilidad = Habilidad.objects.get(id=hab_id)

    if request.method == 'POST':
        habilidad.delete()
        return redirect('habilidades')  # Aquí, asegúrate de que el nombre de la vista sea correcto

    return render(request, 'eliminar_habilidad.html', {'habilidad': habilidad})

def sobremi(request):
    print('Hola estoy en sobremi')
    nombre = 'vicky'
    edad=27
    telefono='648832432'
    cargo='Admistrativo'
    # hacemos select de las categorias para cogerlo de la otra tabla
    listarCategorias = Categoria.objects.all().order_by('-nombre_categoria')
    # ahora hacemos bucle para ver las categorias
    for r in listarCategorias:
        print(str(r.nombre_categoria)) #siempre incluir la funcion str para que no de fallo
    context = {'nombre': nombre,'edad':edad,'telefono':telefono,'cargo':cargo,'listarCategorias':listarCategorias}
    return render(request, 'sobremi.html', context=context)


def estudios(request):
    # Obtener todos los registros de la tabla 'Estudio', ordenados por el campo 'id' de forma descendente
    estudios_list = Estudio.objects.all().order_by('-id')

    # Crear el paginador con 2 registros por página
    paginator = Paginator(estudios_list, 2)  # Cambiado a 2 para que muestre 2 elementos por página

    # Obtener el número de página de la solicitud
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Obtener la página correspondiente

    # Crear el contexto con la lista completa de estudios
    context = {
        'estudios_list': page_obj,
    }

    # Renderizar el template 'estudios.html' con el contexto
    return render(request, 'estudios.html', context=context)

def experiencia(request):
    # Obtener todos los registros de la tabla 'Estudio', ordenados por el campo 'id' de forma descendente
    experiencia_list = Experiencia.objects.all().order_by('-id')

    # Crear el paginador con 2 registros por página
    paginator = Paginator(experiencia_list, 2)  # Cambiado a 2 para que muestre 2 elementos por página

    # Obtener el número de página de la solicitud
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Obtener la página correspondiente

    # Crear el contexto con la lista completa de estudios
    context = {
        'experiencia_list': page_obj,
    }

    # Renderizar el template 'experiencia_list' con el contexto
    return render(request, 'experiencias.html', context=context)

def ver_experiencia(request,id):
    expe_id=id
    experiencia = Experiencia.objects.get(id=expe_id)
    context = {'experiencia': experiencia}
    return render(request, 'ver_experiencia.html',context=context)

def eliminarExperiencia(request,pk):
    print("ELIMINAR")
    #Creamos variables
    expe_id=pk
    experiencia = Experiencia.objects.get(id=expe_id) #es registro No query set
    #si es un post es que llega, si es un get es que sale de una accion
    if request.method == 'POST':
        experiencia.delete()
        return redirect('experiencia')
    return render(request, 'eliminar_experiencia.html', {'experiencia':experiencia})

def crear_persona(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ap1 = request.POST.get('ap1')
        ap2 = request.POST.get('ap2')
        edad = request.POST.get('edad')

        persona = Persona(nombre=nombre, ap1=ap1, ap2=ap2, edad=edad)
        persona.save()
        return redirect('lista_personas') # Redirije a la lista de personas o a otra paguina
        return render(request, 'crear_persona.html')
        #vista para editar una persona existente

def editar_persona(request, persona_id):
    persona = get_object_or_404(Persona, id=persona_id)

    if request.method == 'POST':
        persona.nombre = request.POST.get('nombre')
        persona.ap1 = request.POST.get('ap1')
        persona.ap2 = request.POST.get('ap2')
        persona.edad = request.POST.get('edad')
        persona.save()
        return redirect('lista_personas') #Redirige a la lista de personas o a otra pagina
        return render(request, 'editar_persona.html', {'persona':persona})

def login_view(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login') #redirige al login una vez registrado
    return render(request, 'register.html')

#Cerrar la sesion del usuario
def cerrar(request):
    username = request.user.username
    password = request.user.password
    idusuario = request.user.id
    print("logout.............."+username+"clave="+str(password)+"id="+str(idusuario))
    user = authenticate(request, username=username, password=password)
    #desconectamos al usuario
    logout(request)
    return redirect('/')

def subir_imagenes(request):
    idUsuario = request.session['idusuario']
    if request.method == 'POST':
        imagenes = request.FILES.getlist('imagenes')

        for imagen in  imagenes:
            if imagen.name.endswith(('.png','.jpg','.jpeg','.gif','.jfif','.JPG')):
                print('entra')
                img = Imagen()
                img.imagen = imagen
                img.save()
        return redirect('subir_imagenes')
    imagenes = Imagen.objects.all()
    return render(request, 'subir_imagenes.html', {'imagenes': imagenes})
def eliminar_imagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, id=imagen_id)
    if request.method == 'POST':
        imagen.delete()
        return redirect('subir_imagenes') #redirige a la galería de imagenes
    return redirect('subir_imagenes') #redirige a la galeria de imagenes
def editar_imagen(request, imagen_id):
    imagen = get_object_or_404(Imagen, id=imagen_id)
    if request.method =='POST' and request.FILES.get('nueva_imagen'):
        #Actualizamos la imagen
        imagen.imagen = request.FILES['nueva_imagen']
        imagen.save()
        return redirect('subir_imagenes') #Redirige a la galeria de imagenes
    return redirect('subir_imagenes')

def subir_videos(request):
    if request.method == 'POST' and request.FILES['videos']:
        videos = request.FILES.getlist('videos')

        for video in  videos:
            if video.name.endswith(('.mp3','.mp4','.mov','.avi','.mkv')):
                v = Video()
                v.video = video
                v.save()
        return redirect('subir_videos')
    videos = Video.objects.all()
    return render(request, 'subir_videos.html', {'videos': videos})
def eliminar_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('subir_videos')
    return redirect('subir_videos')
def editar_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method =='POST' and request.FILES.get('nuevo_video'):
        #Actualizamos el video
        video.video == request.FILES['nuevo_video']
        video.save()
        return redirect('subir_videos') #Redirige a la galeria de imagenes
    return redirect('subir_videos')
def login_view(request):
    print("Logi_view")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            actual = request.user #usuario actual
            idusuario = 0
            idusuario = actual.id
            request.session['idusuario'] = idusuario
            print("idusuario="+str(idusuario))
            entrevistador = Entrevistador.objects.get(user=idusuario)
            idEntrevistador = entrevistador.id
            print("idEntrevistador="+str(idEntrevistador))
            print("FOTO="+str(entrevistador.avatar))
            fotoperfil = settings.MEDIA_URL + str(entrevistador.avatar) if entrevistador.avatar else settings.MEDIA_URL + "MONEDA3.jpg"
            print("avatar="+str(fotoperfil))
            context = {'fotoperfil':fotoperfil}
            return render(request, 'home.html', context=context)
        #return redirect('home')
        else:
            return render(request, 'login.html',{'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        context = {'nombre':nombre,'email':email,'asunto':asunto,'mensaje':mensaje}
        template = render_to_string('email_template.html', context=context)

        email = EmailMessage(asunto,template,settings.EMAIL_HOST_USER,['vicky.dam2024@gmail.com'])

        email.fail_silenty = False #que no marque error en gmail
        email.send()

        messages.success(request, 'Se ha enviado tu email')
        return redirect('home')
    return render(request, 'correo.html')