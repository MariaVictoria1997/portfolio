# -*-coding: utf-8 -*-
from __future__ import unicode_literals

import os  # Manejo de archivos y rutas
from django.conf import settings  # Configuración global del proyecto
from django.shortcuts import render, get_object_or_404, redirect  # Funciones para vistas
from django.http import HttpResponse  # Respuesta HTTP
from django.core.paginator import Paginator  # Paginación
from django.contrib.auth.models import User  # Modelo de usuario
from django.contrib.auth import authenticate, login, logout  # Autenticación
from django.contrib import messages  # Mensajes de Django
from django.core.mail import EmailMessage  # Para envío de emails
from django.template.loader import render_to_string  # Renderizado de plantillas para email
from reportlab.lib.pagesizes import letter  # Tamaño de página PDF
from reportlab.pdfgen import canvas  # Generador de PDF
from reportlab.lib import colors  # Colores para el PDF
from reportlab.lib.utils import ImageReader  # Para insertar imágenes en PDFs
from appportfolio.models import * #importamos el modelo de todos
# Importar modelos de la aplicación
from appportfolio.models import Entrevistador, Curriculum, DetalleCurriculumEstudio, DetalleCurriculumExperiencia, Estudio
from django.shortcuts import render, get_object_or_404, redirect
from .models import Valoracion
#para el chat
from django.http import JsonResponse
#para que funcionen los decorados
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#para tareas
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea, Estado
from django.http import HttpResponse
from django.utils.timezone import now
from django.shortcuts import render, redirect
from .forms import TareaForm



# Create your views here.
################################################
# HOME
################################################
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
################################################
# HABILIDADES
################################################
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

def editar_habilidad(request, pk):
    habilidad = get_object_or_404(Habilidad, pk=pk)
    if request.method == 'POST':
        habilidad.habilidad = request.POST.get('habilidad')
        habilidad.nivel = request.POST.get('nivel')
        habilidad.comentario = request.POST.get('comentario')
        habilidad.save()
        return redirect('habilidades')

    return render(request, 'editar_habilidad.html', {'habilidad': habilidad})
def eliminar_habilidad(request, pk):
    print("ELIMINAR")
    hab_id = pk
    habilidad = Habilidad.objects.get(id=hab_id)

    if request.method == 'POST':
        habilidad.delete()
        return redirect('habilidades')  # Aquí, asegúrate de que el nombre de la vista sea correcto

    return render(request, 'eliminar_habilidad.html', {'habilidad': habilidad})
################################################
# SOBRE MI
################################################
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

################################################
# ESTUDIOS
################################################
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

def ver_estudio(request, id):
    estudio = get_object_or_404(Estudio, id=id)
    return render(request, 'ver_estudios.html', {'estudio': estudio})

def editar_estudio(request, id):
    estudio = get_object_or_404(Estudio, id=id)
    if request.method == 'POST':
        estudio.titulacion = request.POST.get('titulacion')
        estudio.fechaInicio = request.POST.get('fechaInicio')
        estudio.fechaFin = request.POST.get('fechaFin')
        estudio.notaMedia = request.POST.get('notaMedia')
        estudio.lugarEstudio = request.POST.get('lugarEstudio')
        estudio.nombreLugar = request.POST.get('nombreLugar')
        estudio.ciudad = request.POST.get('ciudad')
        estudio.presencial = request.POST.get('presencial') == 'on'
        estudio.observaciones = request.POST.get('observaciones')
        estudio.save()
        return redirect('estudios')
    return render(request, 'editar_estudio.html', {'estudio': estudio})

def eliminar_estudio(request, id):
    estudio = get_object_or_404(Estudio, id=id)
    estudio.delete()
    return redirect('estudios')
################################################
# EXPERIENCIA
################################################
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

def eliminarExperiencia(request, pk):
    experiencia = get_object_or_404(Experiencia, pk=pk)
    if request.method == 'POST':
        experiencia.delete()
        return redirect('experiencia')  # Asegúrate de que el nombre coincide con la vista de la lista.
    return render(request, 'eliminar_experiencia.html', {'experiencia': experiencia})
################################################
# PERSONA
################################################
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
################################################
# LOGIN
################################################
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
################################################
# REGISTRAR
################################################
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('login') #redirige al login una vez registrado
    return render(request, 'register.html')

################################################
# CERRAR SESION
################################################
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
################################################
# IMAGEN
################################################
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
################################################
# VIDEOS
################################################
def subir_videos(request):
    if request.method == 'POST':
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
    print("entra"+str(video_id))
    video = get_object_or_404(Video, id=video_id)
    if request.method =='POST' and request.FILES.get('nuevo_video'):
        #Actualizamos el video
        video.video == request.FILES['nuevo_video']
        print("entra" + str(video.video)).
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
################################################
# MAIL
################################################
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
        return redirect('contacto')
    return render(request, 'correo.html')
################################################
# ENTREVISTADOR
################################################
def listar_entrevistadores(request):
    entrevistadores = Entrevistador.objects.all()
    return render(request, 'listar_entrevistadores.html', {'entrevistadores':entrevistadores})

# Generar PDF para Entrevistador
def generar_pdf_entrevistador(request, entrevistador_id):
    entrevistador = get_object_or_404(Entrevistador, id=entrevistador_id)

    # Crear una respuesta HTTP con contenido tipo PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="entrevistador_{entrevistador.id}.pdf"'

    # Crear el objeto canvas de ReportLab
    p = canvas.Canvas(response, pagesize=letter)

    # Configuración del título
    p.setFont("Helvetica-Bold", 16)
    p.setFillColor(colors.darkblue)
    p.drawCentredString(300, 770, "Reporte de Entrevistador")

    # Volver al tamaño de fuente normal
    p.setFont("Helvetica", 12)
    p.setFillColor(colors.black)

    # Datos del entrevistador
    p.drawString(100, 720, f"ID: {entrevistador.id}")
    p.drawString(100, 700, f"Empresa: {entrevistador.empresa or 'N/A'}")
    p.drawString(100, 680, f"Fecha de entrevista: {entrevistador.fecha_entrevista or 'N/A'}")
    p.drawString(100, 660, f"Conectado: {'Sí' if entrevistador.conectado else 'No'}")
    p.drawString(100, 640, f"Seleccionado: {'Sí' if entrevistador.seleccionado else 'No'}")
    p.drawString(100, 620, f"Usuario: {entrevistador.user.username if entrevistador.user else 'N/A'}")

    # Añadir avatar si existe
    if entrevistador.avatar and os.path.exists(entrevistador.avatar.path):
        p.drawImage(entrevistador.avatar.path, 100, 500, width=100, height=100)

    # Guardar el PDF
    p.showPage()
    p.save()

    return response

################################################
# CURRICULUM
################################################
# Vista para agregar un curriculum
def agregar_curriculum(request):
    personal = Personal.objects.get(id=1)
    if request.method == 'POST':
        #nombre = request.POST.get('nombre') cajita
        #ap1 = request.POST.get('ap1')
        #ap2 = request.POST.get('ap2')
        nombre=personal.nombre #interno del id
        ap1=personal.apellido1
        ap2=personal.apellido2
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        curriculum = Curriculum(nombre=nombre, ap1=ap1, ap2=ap2, email=email, telefono=telefono)
        curriculum.save()

        return redirect('ver_curriculum', id=personal.id)
    return render(request, 'agregar_curriculum.html')


# Controlador para ver el curriculum
def ver_curriculum(request, id):
    curriculum = get_object_or_404(Curriculum, id=id)
    estudios = DetalleCurriculumEstudio.objects.filter(curriculum=curriculum)
    experiencias = DetalleCurriculumExperiencia.objects.filter(curriculum=curriculum)
    context = {'curriculum': curriculum, 'estudios': estudios, 'experiencias': experiencias}
    return render(request, 'ver_curriculum.html', context=context)


# Controlador para generar el PDF del curriculum
def generar_pdf(request, entrevistador_id):
    curriculum = get_object_or_404(Curriculum, id=entrevistador_id)
    estudios = DetalleCurriculumEstudio.objects.filter(curriculum=curriculum)
    experiencias = DetalleCurriculumExperiencia.objects.filter(curriculum=curriculum)

    # Crear la respuesta HttpResponse con el tipo contenido PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="curriculum_{curriculum.nombre}_{curriculum.ap1}.pdf"'

    # Crear un objeto canvas de ReportLab para generar el PDF
    c = canvas.Canvas(response, pagesize=letter)
    width, height = letter

    # Cargar imagen de avatar
    avatar_path = os.path.join(settings.MEDIA_ROOT, "MEDIA/moneda3.jpg")
    if os.path.exists(avatar_path):
        avatar = ImageReader(avatar_path)
        c.drawImage(avatar, width - 150, height - 150, width=100, height=100)

    # Título del curriculum en color
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(colors.HexColor("#4B8BBE"))
    c.drawString(100, height - 100, f"Curriculum de {curriculum.nombre} {curriculum.ap1}")

    # Información de contacto en color diferente
    c.setFont("Helvetica", 12)
    c.setFillColor(colors.HexColor("#306998"))
    c.drawString(100, height - 130, f"Email: {curriculum.email}")
    c.drawString(100, height - 150, f"Teléfono: {curriculum.telefono}")

    # Sección de estudios en otro color
    y_position = height - 200
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor("#FFDD43"))
    c.drawString(100, y_position, "Estudios:")

    # Mostrar cada estudio con detalles
    c.setFont("Helvetica", 12)
    y_position -= 20
    for estudio in estudios:
        if y_position < 100:
            c.showPage()
            y_position = height - 100
        c.setFillColor(colors.black)
        c.drawString(100, y_position, f"{estudio.estudio.titulacion} ({estudio.estudio.fechaInicio} - {estudio.estudio.fechaFin})")
        y_position -= 20

    # Sección de experiencia laboral
    y_position -= 40
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.HexColor("#306998"))
    c.drawString(100, y_position, "Experiencia laboral:")
    y_position -= 20
    c.setFont("Helvetica", 12)
    for experiencia in experiencias:
        if y_position < 100:
            c.showPage()
            y_position = height - 100
        c.setFillColor(colors.black)
        c.drawString(100, y_position, f"{experiencia.experiencia.empresa} ({experiencia.experiencia.fecha_inicio} - {experiencia.experiencia.fecha_fin})")
        y_position -= 20

    # Finalizar el PDF
    c.showPage()
    c.save()

    return response

################################################
# NOTICIAS
################################################
# Vista para ver las noticias
def lista_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_creacion')
    return render(request, 'lista_noticias.html', {'noticias': noticias})


# Vista para crear una nueva noticia
def crear_noticia(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        imagen = request.FILES.get('imagen')

        if titulo and contenido:
            noticia = Noticia.objects.create(titulo=titulo, contenido=contenido, imagen=imagen)
            return redirect('lista_noticias')
        else:
            return HttpResponse("Error: el título y el contenido son obligatorios.", status=400)

    return render(request, 'crear_noticia.html')
################################################
# VALORACIONES
################################################
def listar_valoraciones(request):
    valoraciones = Valoracion.objects.all()
    return render(request, 'list.html', {'valoraciones': valoraciones})


def actualizar_valoracion(request, pk):
    valoracion = get_object_or_404(Valoracion, pk=pk)
    if request.method == "POST":
        votos_entrevista = int(
            request.POST.get("votos_entrevista", valoracion.votos_entrevista)
        )
        votos_empresa = int(
            request.POST.get("votos_empresa", valoracion.votos_empresa)
        )
        # Actualizar los votos y recalcular la media
        valoracion.votos_entrevista = votos_entrevista
        valoracion.votos_empresa = votos_empresa
        valoracion.media_aspectos = (votos_entrevista + votos_empresa) / 2
        valoracion.save()
        return redirect('listar_valoraciones')

    return render(request, 'update.html', {'valoracion': valoracion})

def añadir_valoracion(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        entrevista = request.POST.get('entrevista')
        empresa = request.POST.get('empresa')
        votos_entrevista = int(request.POST.get('votos_entrevista', 0))
        votos_empresa = int(request.POST.get('votos_empresa', 0))

        # Calcular la media de los aspectos
        media_aspectos = (votos_entrevista + votos_empresa) / 2

        # Crear y guardar la nueva valoración
        Valoracion.objects.create(
            entrevista=entrevista,
            empresa=empresa,
            votos_entrevista=votos_entrevista,
            votos_empresa=votos_empresa,
            media_aspectos=media_aspectos
        )

        return redirect('listar_valoraciones')

    return render(request, 'add.html')
################################################
# CHAT
################################################
#Seleccionar entrevistador chat
@login_required
def seleccionar_entrevistadores(request):
    entrevistadores = Entrevistador.objects.all()
    # Si el usuario está enviando un formulario, redirigir al chat con el entrevistador seleccionado
    if request.method == 'POST':
        entrevistador_id = request.POST.get('entrevistador_id')
        return redirect('chat_view', entrevistador_id=entrevistador_id)
    return render(request, 'seleccionar_entrevistador.html', {'entrevistadores': entrevistadores})
#ayuda a que los usuarios estén logeados por fuerta @login_required
@login_required
def chat_view(request, entrevistador_id):
    entrevistador = get_object_or_404(Entrevistador, id=entrevistador_id) #es como un select
    mensajes = Mensaje.objects.filter( #la funcion Q sirve para que pueda hacer multiples condiciones
        (models.Q(remitente=request.user) & models.Q(destinatario=entrevistador.user)) |
         (models.Q(remitente=entrevistador.user) & models.Q(destinatario=request.user))
    )
    #Agregar la propiedad 'clase' para usarla en el template
    for mensaje in mensajes:
        mensaje.clase = 'enviado' if mensaje.remitente == request.user else 'recibido'
    # Renderizar solo el chat para la respuesta AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'mensajesHtml': render_to_string('chat_mensajes.html', {'mensajes':mensajes}),
        })
    return render(request,'chat.html', {'entrevistador':entrevistador, 'mensajes':mensajes})

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        destinatario_id = request.POST.get('destinatario_id')
        destinatario = get_object_or_404(User, id=destinatario_id)
        print(f"Contenido: {contenido}, Destinatario ID: {destinatario_id}")
        mensaje = Mensaje.objects.create(
            remitente = request.user,
            destinatario=destinatario,
            contenido=contenido
        )
        return JsonResponse({'status': 'success', 'mensaje': mensaje.contenido, 'fecha_envio': mensaje.fecha_envio})
    return JsonResponse({'status': 'error', 'message': 'Metodo no permitido'})

################################################
# TREAS
################################################
@login_required
def listar_tareas(request):
    tareas = Tarea.objects.all()  # Obtén todas las tareas de la base de datos
    return render(request, 'listar_tareas.html', {'tareas': tareas})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        tarea_nombre = request.POST.get('tarea')
        fecha = request.POST.get('fecha')
        estado_id = request.POST.get('estado')

        # Obtener el estado correspondiente
        estado = Estado.objects.get(id=estado_id)

        # Crear la tarea y guardarla en la base de datos
        tarea = Tarea(tarea=tarea_nombre, fecha=fecha, estado=estado)
        tarea.save()

        # Redirigir a la lista de tareas
        return redirect('listar_tareas')

    else:
        estados = Estado.objects.all()  # Obtenemos todos los estados para el formulario
        return render(request, 'crear_tarea.html', {'estados': estados})

@login_required
def editar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)

    if request.method == 'POST':
        tarea.tarea = request.POST.get('tarea')
        tarea.fecha = request.POST.get('fecha')
        tarea.estado = Estado.objects.get(id=request.POST.get('estado'))  # Actualizar el estado
        tarea.save()

        return redirect('listar_tareas')  # Redirigir a la lista de tareas

    # Si es un GET, mostrar el formulario con los datos actuales
    estados = Estado.objects.all()
    return render(request, 'editar_tarea.html', {'tarea': tarea, 'estados': estados})

@login_required
def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()  # Elimina la tarea de la base de datos
    return redirect('listar_tareas')  # Redirigir a la lista de tareas
################################################
# CALIFICACIONES
################################################
def lista_calificaciones(request):
    calificaciones = Calificacion.objects.all().order_by('-nota')
    Totmedia = 0
    i = 0

    for media in calificaciones:
        Totmedia += media.nota
        i += 1

    # Calcula el promedio solo si hay calificaciones
    promedio = Totmedia / i if i > 0 else None

    context = {
        'calificaciones': calificaciones,
        'promedio': promedio
    }
    return render(request, 'lista_calificaciones.html', context=context)

def añadir_calificacion(request):
    if request.method == 'POST':
        asignatura = request.POST.get('asignatura')
        nota = request.POST.get('nota')
        if asignatura and nota:
            Calificacion.objects.create(asignatura=asignatura, nota=nota)
        return redirect('lista_calificaciones')  # Asegúrate de que redirige aquí
    return render(request, 'agregar_calificacion.html')
