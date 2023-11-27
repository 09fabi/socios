"""
URL configuration for socios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app_socios import views
from app_socios.views import listado, agregar_socio, eliminar_socio, actualizar_socio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('listado/', listado, name='listado'),
    path('agregar/', agregar_socio, name='agregar'),
    path('listado/agregar/', agregar_socio, name='agregar'),
    path('eliminar_socio/<int:id>/', eliminar_socio, name='eliminar_socio'),
    path('actualizar_socio/<int:id>/', actualizar_socio, name='actualizar_socio'),
]
