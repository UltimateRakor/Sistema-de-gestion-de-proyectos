"""
URL configuration for pruebav2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Gestio_proyectos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('registro/', views.registro, name="Registro"),
    path('inicio_sesion/', views.inicio_sesion, name="inicio_sesion"),
    path('cerrar_sesion/', views.cerrar_sesion, name="logout"),
    path('menu_proyectos/', views.menu_proyectos, name="menu_proyectos"),
    path('crear_proyecto/', views.crear_proyecto, name="crear_proyecto"),
    path('listar_proyectos/', views.listar_proyectos, name="listar_proyectos"),
    path('eliminar_proyecto/<int:proyecto_id>/', views.eliminar_proyecto, name="eliminar_proyecto"),
    path('menu_equipo/', views.menu_equipo, name="menu_equipo"),
    path('crear_equipo/', views.crear_equipo, name="crear_equipo"),
    path('listar_equipos/', views.listar_equipos, name="listar_equipos"),
    path('eliminar_equipo/<int:equipo_id>/', views.eliminar_equipo, name="eliminar_equipo"),
    path('crear_tarea/', views.crear_tarea, name="crear_tarea"),
    path('eliminar_tarea/<int:tarea_id>/', views.eliminar_tarea, name="eliminar_tarea"),
    path('menu_tareas/', views.menu_tareas, name="menu_tareas"),
    path('listar_tareas/', views.listar_tareas, name='listar_tareas'),

]


