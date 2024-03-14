from django.urls import path
from .views import crear_usuario, editar_contraseña, cerrar_sesion, ver_perfil, iniciar_sesion, editar_perfil

urlpatterns = [
    path('login/', iniciar_sesion , name='iniciar_sesion'),
    path('registro/', crear_usuario, name='registrar'),
    path('logout/', cerrar_sesion, name='logout'),
    path('perfil/', ver_perfil, name='ver_perfil'),
    path('editar_perfil/', editar_perfil, name = 'editar_perfil' ),
    path('editar_pass/', editar_contraseña, name='editar_pass'),
    
]