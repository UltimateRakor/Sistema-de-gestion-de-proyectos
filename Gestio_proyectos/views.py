from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db import IntegrityError
from .form import ProyectoForm,EquipoForm,TareaForm
from .models import Tarea,Equipo,Proyecto
from django.contrib.auth.decorators import login_required

# Crear tus vistas aquí.
def home(request):
    return render(request, 'home.html')
    

def registro(request):
    if request.method == 'GET':
        return render(request, 'Registro.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'Registro.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'Registro.html', {"form": UserCreationForm, "error": "Passwords did not match."})


def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "El nombre de usuario o la contraseña son incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, 'inicio_sesion.html', {'form': form})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('home')



#funciones proyecto
@login_required
def menu_proyectos(request):
    return render(request, 'menu_proyectos.html')


@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ProyectoForm()
    
    return render(request, 'crear_proyecto.html', {'form': form})

@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)

    if request.method == 'POST':
        proyecto.delete()  # Eliminar el proyecto
        return redirect('home')  # Redirigir a la página principal después de eliminar

    return render(request, 'confirmar_eliminar_proyecto.html', {'proyecto': proyecto})

@login_required
def listar_proyectos(request):
    proyectos = Proyecto.objects.all()  # Obtener todos los proyectos
    return render(request, 'listar_proyectos.html', {'proyectos': proyectos})




#funciones equipo
@login_required
def menu_equipo(request):
    return render(request, 'menu_equipo.html')

@login_required
def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home') 
    else:
        form = EquipoForm()  

    return render(request, 'crear_equipo.html', {'form': form})

@login_required
def listar_equipos(request):
    equipos = Equipo.objects.all()  # Obtén todos los equipos
    return render(request, 'listar_equipos.html', {'equipos': equipos})


@login_required
def eliminar_equipo(request, equipo_id):
    # Obtener el equipo o devolver un error 404 si no se encuentra
    equipo = get_object_or_404(Equipo, pk=equipo_id)

    if request.method == 'POST':
        equipo.delete()  # Eliminar el equipo
        return redirect('menu_equipo')  # Redirigir al menú de equipos después de eliminar

    return render(request, 'confirmar_eliminar_equipo.html', {'equipo': equipo})



#funciones tarea

@login_required
def menu_tareas(request):
    return render(request, 'menu_tareas.html')

@login_required
def listar_tareas(request):
    tareas = Tarea.objects.all()  # O filtrar según el usuario
    return render(request, 'listar_tareas.html', {'tareas': tareas})


@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('home')  
    else:
        form = TareaForm()  

    return render(request, 'crear_tarea.html', {'form': form})



@login_required
def eliminar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id, responsable=request.user)

    if request.method == 'POST':
        tarea.delete()  
        return redirect('home')  

    return render(request, 'confirmar_eliminar.html', {'tarea': tarea})
